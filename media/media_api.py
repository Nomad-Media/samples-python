from nomad_media_pip.src.nomad_sdk import Nomad_SDK
from config import config

nomad_sdk = Nomad_SDK(config)

import json

def get_input(prompt, required):
    return input(f"Enter {prompt}: ") if required or input(f"Do you want to add {prompt} (y/n): ") == "y" else None

def get_bool(prompt):
    return True if input(f"{prompt} (y/n): ") == "y" else False

def get_list(prompt, required):
    items = []
    if required or input(f"Do you want to add a {prompt} (y/n): ") == "y":
        while True:
            items.append(input(f"{prompt}: "))
            if not required or input(f"Do you want to add another {prompt} (y/n): ") == "n":
                break
    
    return items

def clear_continue_watching():
    try:
        USER_ID = input(f"Enter user id: ") if input("Do you want to use another user's id (y/n): ") == "y" else None
        ASSET_ID = get_input("asset id", False)

        nomad_sdk.clear_continue_watching(USER_ID, ASSET_ID)
    except:
        raise Exception()
    
def clear_watchlist():
    try:
        USER_ID = input(f"Enter user id: ") if input("Do you want to use another user's id (y/n): ") == "y" else None
        
        nomad_sdk.clear_watchlist(USER_ID)
    except:
        raise Exception()

def create_form():
    try:
        CONTENT_DEFINITION_ID = get_input("content definition id", True)
        FIRST_NAME = get_input("first name", True)
        LAST_NAME = get_input("last name", True)
        ACTIVE = get_bool("active")
        START_DATE = get_input("start date (YYYY-MM-DDTHH:MM:SS)", True) + "Z"
        DESCRIPTION = get_input("description", True)

        FORMS = nomad_sdk.create_form(CONTENT_DEFINITION_ID, 
            {
                "firstName": FIRST_NAME, 
                "lastName": LAST_NAME, 
                "active": ACTIVE, 
                "startDate": START_DATE, 
                "description": DESCRIPTION
            })
        
        print(json.dumps(FORMS, indent=4))
    except:
        raise Exception()
    
def get_content_cookies():
    try:
        CONTENT_ID = get_input("content id", True)

        COOKIES = nomad_sdk.get_content_cookies(CONTENT_ID)

        print(json.dumps(COOKIES, indent=4))
    except:
        raise Exception()
    
def get_default_site_config():
    try:
        DEFAULT_SITE_CONFIG = nomad_sdk.get_default_site_config()

        print(json.dumps(DEFAULT_SITE_CONFIG, indent=4))
    except:
        raise Exception()
    
def get_dynamic_content():
    try:
        DYNAMIC_CONTENT_RECORD_ID = get_input("dynamic content record id", True)

        DYNAMIC_CONTENT = nomad_sdk.get_dynamic_content(DYNAMIC_CONTENT_RECORD_ID)

        print(json.dumps(DYNAMIC_CONTENT, indent=4))
    except:
        raise Exception()
    
def get_dynamic_contents():
    try:
        DYNAMIC_CONTENTS = nomad_sdk.get_dynamic_contents()

        print(json.dumps(DYNAMIC_CONTENTS, indent=4))
    except:
        raise Exception()
    
def get_media_group():
    try:
        MEDIA_GROUP_ID = get_input("media group id", True)

        MEDIA_GROUP_FILTERS = get_list("filter", False)

        MEDIA_GROUP = nomad_sdk.get_media_group(MEDIA_GROUP_ID, MEDIA_GROUP_FILTERS)

        print(json.dumps(MEDIA_GROUP, indent=4))
    except:
        raise Exception()
    
def get_media_item():
    try:
        MEDIA_ITEM_ID = get_input("media item id", True)

        MEDIA_ITEM = nomad_sdk.get_media_item(MEDIA_ITEM_ID)

        print(json.dumps(MEDIA_ITEM, indent=4))
    except:
        raise Exception()
    
def get_my_content():
    try:
        MY_CONTENT = nomad_sdk.get_my_content()

        print(json.dumps(MY_CONTENT, indent=4))
    except:
        raise Exception()
    
def get_my_group():
    try:
        GROUP_ID = get_input("group id", True)

        MY_GROUP = nomad_sdk.get_my_group(GROUP_ID)

        print(json.dumps(MY_GROUP, indent=4))
    except:
        raise Exception()
    
def get_site_config():
    try:
        SITE_CONFIG_RECORD_ID = get_input("site config record id", True)

        SITE_CONFIG = nomad_sdk.get_site_config(SITE_CONFIG_RECORD_ID)

        print(json.dumps(SITE_CONFIG, indent=4))
    except:
        raise Exception()
    
def media_search():
    try:
        SEARCH_QUERY = get_input("search query", False)
        id_input = get_input("Ids (separated by comma)", False)
        IDS = id_input.split(",") if id_input else None
        SORT_FIELDS = []
        if input("Do yo want to add a sort field (y/n): ") == "y":
            while True:
                SORT_FIELDS_NAME = input("Enter the field name you want to sort by: ")
                SORT_FIELDS_ORDER = input("Enter the order you want to sort the field by (ascending/descending)")

                SORT_FIELDS.append({
                    "fieldName": SORT_FIELDS_NAME,
                    "sortType": SORT_FIELDS_ORDER
                })
                if input("Do yo want to add another sort field (y/n): ") == "n":
                    break

        OFFSET = get_input("offset", False)
        SIZE = get_input("size", False)

        MEDIA = nomad_sdk.media_search(SEARCH_QUERY, IDS, SORT_FIELDS,
                                       OFFSET, SIZE)
        
        print(json.dumps(MEDIA, indent=4))
    except:
        raise Exception()

functions = {
    "1": clear_continue_watching,
    "2": clear_watchlist,
    "3": create_form,
    "4": get_content_cookies,
    "5": get_default_site_config,
    "6": get_dynamic_content,
    "7": get_dynamic_contents,
    "8": get_media_group,
    "9": get_media_item,
    "10": get_my_content,
    "11": get_my_group,
    "12": get_site_config,
    "13": media_search
}

if __name__ == "__main__":
    print("Which function do you want to run?")
    for key, value in functions.items():
        print(f"{key}: {value.__name__}")

    while True:
        USER_INPUT = input("Enter the number of the function you want to run: ")

        if USER_INPUT in functions:
            functions[USER_INPUT]()
            break
        else:
            print("Invalid input")