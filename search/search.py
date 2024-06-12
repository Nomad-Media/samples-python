from nomad_media_pip.src.nomad_sdk import Nomad_SDK
from config import config

nomad_sdk = Nomad_SDK(config)

from helpers.get_search_result import get_search_result

import json

def search():
    try:
        PAGE_OFFSET = input("Enter page offset: ") if input("Do you want to add a page offset (y/n): ") == "y" else None
        PAGE_SIZE = input("Enter page size: ") if input("Do you want to add a page size (y/n): ") == "y" else None

        SEARCH_QUERY = input("Enter a search query: ") if input("Do you want to add a search query (y/n): ") == "y" else None

        FILTER_YN = True if input("Do you want to add a filter (y/n)?: ") == "y" else False

        FILTERS = []
        #fieldName1 = "contentDefinitionId"
        #operator1="Equals"
        #value1="eb710e28-7c44-492e-91f9-8acd0cd9331c"
        #print(f"Enter field name: {fieldName1}")
        #print(f"Enter operator: {operator1}")
        #print(f"Enter value: {value1}")
        #filter1 = { 
        #        "fieldName": fieldName1,
        #        "operator": operator1,
        #        "values": value1
        #    }
        #FILTERS.append(filter1)
#
        #fieldName2 = "languageId"
        #value2="c66131cd-27fc-4f83-9b89-b57575ac0ed8"
        #print(f"Enter field name: {fieldName2}")
        #print(f"Enter operator: {operator1}")
        #print(f"Enter value: {value2}")
        #filter2 = { 
        #        "fieldName": fieldName2,
        #        "operator": operator1,
        #        "values": value2
        #    }
        #FILTERS.append(filter2)

        while FILTER_YN:
            FIELD_NAME = input("Enter field name: ")
            OPERATOR = input("Enter operator: ")
            VALUE = input("Enter value: ")

            FILTER = { 
                "fieldName": FIELD_NAME,
                "operator": OPERATOR,
                "values": VALUE
            }

            FILTERS.append(FILTER)

            if input("Do you want to add another field (y/n)?: ") != "y": 
                break

        SORT_FIELDS = []
        while True:
            if input(f"Do you want to sort a{"nother" if len(SORT_FIELDS) > 0 else ""} field (y/n): ") == "y":
                SORT_FIELDS_NAME = input("Enter a field name you want to sort by: ")
                SORT_FIELDS_ORDER = input("Enter the order you want to sort the field by (ascending/descending): ")

                SORT_FIELDS.append(
                    {
                        "fieldName": SORT_FIELDS_NAME, 
                        "sortOrder": SORT_FIELDS_ORDER
                    })
            else:
                break

        RESULT_FIELDS_YN = True if input("Do you want to enter the names of the fields you want to "\
                                      "include in your search results (y/n)?: ") == "y" else False

        RESULT_FIELDS = []
        if RESULT_FIELDS_YN: 
            while True:
                RESULT_FIELDS.append(get_search_result())

                if input("Do you want to add another search result field (y/n)?: ") != "y":
                    break

        SIMILAR_ASSET_ID = input("Enter an asset id to find similar assets: ") if input("Do you want to find similar assets (y/n): ") == "y" else None
        MIN_SCORE = input("Enter a minimum score: ") if input("Do you want to add a minimum score (y/n): ") == "y" else None
        EXCLUDE_TOTAL_RECORD_COUNT = input("Do you want to exclude the total record count (y/n): ") == "y"
        FILTER_BINDER = input("Enter a filter binder: ") if input("Do you want to add a filter binder (y/n): ") == "y" else None
        FULL_URL_FIELD_NAMES = input("Enter full url field names (separate by commas): ") if input("Do you want to add full url field names (y/n): ") == "y" else None
        DISTINCT_ON_FIELD_NAME = input("Enter a field name to find distinct values: ") if input("Do you want to find distinct values (y/n): ") == "y" else None
        INCLUDE_VIDEO_CLIPS = input("Do you want to include video clips (y/n): ") == "y"
        USE_LLM_SEARCH = input("Do you want to use LLM search (y/n): ") == "y"
        INCLUDE_INTERNAL_FIELDS_IN_RESULTS = input("Do you want to include internal fields in results (y/n): ") == "y"

        FULL_URL_FIELD_NAMES = FULL_URL_FIELD_NAMES.split(",") if FULL_URL_FIELD_NAMES else None
        if INCLUDE_INTERNAL_FIELDS_IN_RESULTS != "y": INCLUDE_INTERNAL_FIELDS_IN_RESULTS = None

        print("Searching")
        CONTENT = nomad_sdk.search(SEARCH_QUERY, PAGE_OFFSET, PAGE_SIZE, FILTERS, 
            SORT_FIELDS, RESULT_FIELDS, FULL_URL_FIELD_NAMES, DISTINCT_ON_FIELD_NAME, 
            INCLUDE_VIDEO_CLIPS, SIMILAR_ASSET_ID, MIN_SCORE, EXCLUDE_TOTAL_RECORD_COUNT, 
            FILTER_BINDER, USE_LLM_SEARCH, INCLUDE_INTERNAL_FIELDS_IN_RESULTS)
        
        print(json.dumps(CONTENT, indent=4))
    except:
        raise Exception()
    
if __name__ == "__main__":
    search()
