from nomad_media_pip.nomad_sdk import Nomad_SDK
from config import config

nomad_sdk = Nomad_SDK(config)

import json

def get_content_definitions():
    try:
        CONTENT_MANAGEMENT_TYPE = input("Enter content management type: (None, Data Selector, or Form Selector): ") if input("Do you want to add content management type (y/n): ") == "y" else None
        SORT_COLUMN = input("Enter sort column: ") if input("Do you want to add sort column (y/n): ") == "y" else None
        IS_DESC = input("Enter is desc: (True or False): ") if input("Do you want to add is desc (y/n): ") == "y" else None
        PAGE_INDEX = input("Enter page index: ") if input("Do you want to add page index (y/n): ") == "y" else None
        PAGE_SIZE = input("Enter page size: ") if input("Do you want to add page size (y/n): ") == "y" else None

        CONTENT_DEFINITIONS = nomad_sdk.get_content_definitions(CONTENT_MANAGEMENT_TYPE, SORT_COLUMN, 
            IS_DESC == "True", PAGE_INDEX, PAGE_SIZE)
        
        print(json.dumps(CONTENT_DEFINITIONS, indent=4))
    except Exception as e:
        print(f"Error: {e}")

def get_content_definition():
    try:
        CONTENT_DEFINITION_ID = input("Enter content definition id: ")

        CONTENT_DEFINITION = nomad_sdk.get_content_definition(CONTENT_DEFINITION_ID)
        
        print(json.dumps(CONTENT_DEFINITION, indent=4))
    except Exception as e:
        print(f"Error: {e}")

FUNCTIONS = {
    "1": get_content_definitions,
    "2": get_content_definition
}

if __name__ == "__main__":
    print("Which function do you want to run?")
    for key, value in FUNCTIONS.items():
        print(f"{key}: {value.__name__}")

    while True:
        USER_INPUT = input("Enter the number of the function you want to run: ")

        if USER_INPUT in FUNCTIONS:
            FUNCTIONS[USER_INPUT]()
            break
        else:
            print("Invalid input")

