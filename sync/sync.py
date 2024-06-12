import sys, os

sys.path.append(os.path.realpath('...'))

from nomad_media_pip.src.nomad_sdk import Nomad_SDK
from config import config

nomad_sdk = Nomad_SDK(config)

import json
from multiprocessing import Pool

GENRE_CONTENT_DEFINITION_ID = "dbbace1f-ddb1-462b-9cae-c9be7d5990ac"
MOVIE_CONTENT_DEFINITION_ID = "eb710e28-7c44-492e-91f9-8acd0cd9331c"

def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False

    for dict1 in list1:
        if not any(dict1 == dict2 for dict2 in list2):
            return False

    return True

def compare_movies(MOVIE, JSON_MOVIE, GENRES):
    if MOVIE["title"] != JSON_MOVIE["title"]:
        return False
    if MOVIE["identifiers"].get("slugifyField") != JSON_MOVIE["slug"]:
        return False
    if MOVIE["identifiers"].get("plot") != JSON_MOVIE["plot"]:
        return False
    if MOVIE["identifiers"].get("releaseDate") != JSON_MOVIE["releaseDate"]:
        return False
    if MOVIE["identifiers"].get("image") != JSON_MOVIE["image"]:
        return False
    if MOVIE["identifiers"].get("movieFile") != JSON_MOVIE["movieFile"]:
        return False
    if not compare_lists(MOVIE["identifiers"].get("genres"), GENRES):
        return False
    return True

def check_genres(GENRES):
    NOMAD_GENRES = nomad_sdk.search(None, None, None,
        [
            {
                "fieldName":"contentDefinitionId",
                "operator":"Equals",
                "values":GENRE_CONTENT_DEFINITION_ID
            }
        ], None, None, None, None, True, None)

    GENRE_MAP_LIST = []
    for GENRE in GENRES:
        for GENRE_ELEM in NOMAD_GENRES["items"]:
            if GENRE_ELEM["title"] == GENRE:
                GENRE_MAP_LIST.append({ "id": GENRE_ELEM["id"], "description": GENRE_ELEM["title"] })
                break
        else:
            GENRE = nomad_sdk.create_content(GENRE_CONTENT_DEFINITION_ID, None)
            nomad_sdk.update_content(GENRE["contentId"], GENRE_CONTENT_DEFINITION_ID,
                {
                    "title": GENRE
                }, None)
            GENRE_MAP_LIST.append({ "id": GENRE["contentId"], "title": GENRE })

    return GENRE_MAP_LIST

def check_movie(args):
    try:
        idx, JSON_MOVIE, NUM_MOVIES= args
        print(f"Syncing movie #{idx + 1} out of {NUM_MOVIES} | {JSON_MOVIE['title']}")

        MOVIE = next((MOVIE for MOVIE in MOVIES if MOVIE["identifiers"].get("movieId") == JSON_MOVIE["id"]), None)

        # Check if genre exists if not create it
        GENRES = check_genres(JSON_MOVIE["genres"])

        # Check if movie exists
        if (MOVIE is not None):
            if not compare_movies(MOVIE, JSON_MOVIE, GENRES):
                print(f"Updating movie {JSON_MOVIE['title']}")
                MOVIE = nomad_sdk.update_content(MOVIE["id"],
                    MOVIE_CONTENT_DEFINITION_ID,
                    {
                        "title": JSON_MOVIE["title"],
                        "slugifyField": JSON_MOVIE["slug"],
                        "plot": JSON_MOVIE["plot"], 
                        "releaseDate": JSON_MOVIE["releaseDate"], 
                        "genres": GENRES, 
                        "image": JSON_MOVIE["image"], 
                        "movieFile": JSON_MOVIE["movieFile"]
                    }, None)
            else:
                print(f"Movie {JSON_MOVIE['title']} already up to date")
        else:
            print(f"Creating movie {JSON_MOVIE['title']}")
            CONTENT = nomad_sdk.create_content(MOVIE_CONTENT_DEFINITION_ID, None)
            CONTENT_ID = CONTENT["contentId"]
            MOVIE = nomad_sdk.update_content(CONTENT_ID,
                    MOVIE_CONTENT_DEFINITION_ID,
                    {
                        "movieId": JSON_MOVIE["id"],
                        "title": JSON_MOVIE["title"],
                        "slugifyField": JSON_MOVIE["slug"], 
                        "plot": JSON_MOVIE["plot"],
                        "releaseDate": JSON_MOVIE["releaseDate"], 
                        "genres": GENRES, 
                        "image": JSON_MOVIE["image"], 
                        "movieFile": JSON_MOVIE["movieFile"]
                    }, None)
    except Exception as e:
        print(e)


def get_search_result():
    choice = input("Do you want to add a name or a search result field? (name/search): ").lower()

    if choice == "name":
        name = input("Enter the name: ")
        return {"name": name}

    elif choice == "search":
        search_result_name = input("Enter the search result name: ")

        search_result_fields = []
        search_result = get_search_result()
        search_result_fields.append(search_result)

        return {"name": search_result_name, "searchResultFields": search_result_fields}

    else:
        print("Invalid choice. Please enter 'name' or 'search'.")
        return get_search_result()

def get_movies():
    try:
        NOMAD_MOVIES = nomad_sdk.search(None, None, None,
            [
                {
                    "fieldName":"contentDefinitionId",
                    "operator":"Equals",
                    "values":MOVIE_CONTENT_DEFINITION_ID
                }
            ], None, None, None, None, True, None)
        
        if (NOMAD_MOVIES["hasItems"]):
            MOVIES = NOMAD_MOVIES["items"]
        else:
            MOVIES = []

        return MOVIES
    
    except Exception as e:
        raise Exception(f"Error retrieving movies: {e}")

MOVIES = get_movies()

def delete_movie(ID):
    nomad_sdk.delete_content(ID, MOVIE_CONTENT_DEFINITION_ID)

def sync():
    print("Syncronizing...")
    try:
        CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
        MOVIE_PATH = os.path.join(CURRENT_PATH, "movie.json")

        with open(MOVIE_PATH, "r") as movies_file:
            JSON_MOVIES = json.load(movies_file)

        if (JSON_MOVIES is None or len(MOVIES) == 0):
            raise Exception("Error retrieving data, make sure the source file exists and is not empty.")

        print(f"{len(JSON_MOVIES)} movies found in source file")

        for idx, movie in enumerate(JSON_MOVIES):
            check_movie((idx, movie, len(JSON_MOVIES)))

        #with Pool() as pool:
        #    pool.map(check_movie, [(idx, JSON_MOVIE, len(JSON_MOVIES)) for idx, JSON_MOVIE in enumerate(JSON_MOVIES)])

        # Deltes movies that are in delete_ids
        UPDATED_MOVIES = get_movies()

        DELETE_PATH = os.path.join(CURRENT_PATH, "delete_ids.py")

        with open(DELETE_PATH, "r") as delete_file:
            for line in delete_file:
                MOVIE_IDS = json.loads(line)

                for MOVIE_ID in MOVIE_IDS:
                    ID = next((MOVIE["id"] for MOVIE in UPDATED_MOVIES if MOVIE["identifiers"].get("movieId") == MOVIE_ID), None)

                    if (ID is not None):
                        nomad_sdk.delete_content(ID, MOVIE_CONTENT_DEFINITION_ID)
                    else:
                        print(f"Movie with id {MOVIE_ID} not found")

                #with Pool() as pool:
                #    pool.map(delete_movie, ID)

        print("Syncronization completed")
    except Exception as e:
        raise Exception(f"Error syncing movies: {e}")

if __name__ == "__main__":
    sync()
    


