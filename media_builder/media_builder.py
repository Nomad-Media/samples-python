import sys, os
sys.path.append(os.path.realpath('./nomad-samples'))

from nomad_media_pip.src.nomad_sdk import Nomad_SDK
from config import config

nomad_sdk = Nomad_SDK(config)

import json

def get_input(prompt, required):
    return input(f"Enter {prompt}: ") if required or input(f"Do you want to add {prompt} (y/n): ") == "y" else None

def get_bool(prompt):
    return True if input(f"{prompt} (y/n): ") == "y" else False

def create_media_builder():
    try:
        NAME = get_input("name", True)
        DESTINATION_FOLDER_ID = get_input("destination folder id", False)
        COLLECTIONS = get_input("collections", False)
        RELATED_CONTENTS = get_input("related contents", False)
        TAGS = get_input("tags", False)
        PROPERTIES = get_input("properties", False)

        MEDIA_BUILD = nomad_sdk.create_media_builder(NAME, DESTINATION_FOLDER_ID, COLLECTIONS,
            RELATED_CONTENTS, TAGS, PROPERTIES)
        
        print(json.dumps(MEDIA_BUILD, indent=4))
    except:
        raise Exception()
    
def create_media_builder_item():
    try:
        MEDIA_BUILDER_ID = get_input("media builder id", True)
        SOURCE_ASSET_ID = get_input("source asset id", False)
        START_TIME_CODE = get_input("start time code", False)
        END_TIME_CODE = get_input("end time code", False)
        SOURCE_ANNOTATION_ID = get_input("source annotation id", False)
        RELATED_CONTENTS = get_input("related contents", False)

        MEDIA_BUILD_ITEM = nomad_sdk.create_media_builder_item(MEDIA_BUILDER_ID, SOURCE_ASSET_ID,
            START_TIME_CODE, END_TIME_CODE, SOURCE_ANNOTATION_ID, RELATED_CONTENTS)
        
        print(json.dumps(MEDIA_BUILD_ITEM, indent=4))
    except:
        raise Exception()
    
def create_media_builder_items_add_annotations():
    try:
        MEDIA_BUILDER_ID = get_input("media builder id", True)
        SOURCE_ASSET_ID = get_input("source asset id", True)

        MEDIA_BUILD_ITEMS = nomad_sdk.create_media_builder_items_add_annotations(MEDIA_BUILDER_ID, SOURCE_ASSET_ID)

        print(json.dumps(MEDIA_BUILD_ITEMS, indent=4))
    except:
        raise Exception()

def create_media_builder_items_bulk():
    try:
        MEDIA_BUILDER_ID = get_input("media builder id", True)
        MEDIA_BUIDER_ITEMS = []

        while True:
            MEDIA_BUILDER_ITEM = {
                "sourceAssetId": get_input("source asset id", True),
                "startTimeCode": get_input("start time code", True),
                "endTimeCode": get_input("end time code", False)
            }

            MEDIA_BUIDER_ITEMS.append(MEDIA_BUILDER_ITEM)

            if input("Do you want to add another media builder item (y/n): ") == "n":
                break

        MEDIA_BUILD_ITEMS = nomad_sdk.create_media_builder_items_bulk(MEDIA_BUILDER_ID, MEDIA_BUIDER_ITEMS)

        print(json.dumps(MEDIA_BUILD_ITEMS, indent=4))
    except:
        raise Exception()
    
def delete_media_builder():
    try:
        MEDIA_BUILDER_ID = get_input("media builder id", True)

        nomad_sdk.delete_media_builder(MEDIA_BUILDER_ID)
    except:
        raise Exception()
    
def delete_media_builder_item():
    try:
        MEDIA_BUILDER_ID = get_input("media builder id", True)
        MEDIA_BUILDER_ITEM_ID = get_input("media builder item id", True)

        nomad_sdk.delete_media_builder_item(MEDIA_BUILDER_ID, MEDIA_BUILDER_ITEM_ID)
    except:
        raise Exception()
    
def duplicate_media_builder():
    try:
        MEDIA_BUILDER_ID = get_input("media builder id", True)
        NAME = get_input("name", True)
        DESTINATION_FOLDER_ID = get_input("destination folder id", False)
        COLLECTIONS = get_input("collections", False)
        RELATED_CONTENTS = get_input("related contents", False)
        PROPERTIES = get_input("properties", False)

        MEDIA_BUILD = nomad_sdk.duplicate_media_builder(MEDIA_BUILDER_ID, NAME, DESTINATION_FOLDER_ID,
            COLLECTIONS, RELATED_CONTENTS, PROPERTIES)
        
        print(json.dumps(MEDIA_BUILD, indent=4))
    except:
        raise Exception()
    
def get_media_builder():
    try:
        MEDIA_BUILDER_ID = get_input("media builder id", True)

        MEDIA_BUILD = nomad_sdk.get_media_builder(MEDIA_BUILDER_ID)
        
        print(json.dumps(MEDIA_BUILD, indent=4))
    except:
        raise Exception()
    
def get_media_builders():
    try:
        MEDIA_BUILDS = nomad_sdk.get_media_builders()
        
        print(json.dumps(MEDIA_BUILDS, indent=4))
    except:
        raise Exception()
    
def get_media_builder_items():
    try:
        MEDIA_BUILDER_ID = get_input("media builder id", True)

        MEDIA_BUILD_ITEMS = nomad_sdk.get_media_builder_items(MEDIA_BUILDER_ID)
        
        print(json.dumps(MEDIA_BUILD_ITEMS, indent=4))
    except:
        raise Exception()
    
def move_media_builder_item():
    try:
        MEDIA_BUILDER_ID = get_input("media builder id", True)
        MEDIA_BUILDER_ITEM_ID = get_input("media builder item id", True)
        PREVIOUS_MEDIA_BUILDER_ITEM_ID = get_input("previous media builder item id", False)

        nomad_sdk.move_media_builder_item(MEDIA_BUILDER_ID, MEDIA_BUILDER_ITEM_ID,
            PREVIOUS_MEDIA_BUILDER_ITEM_ID)
    except:
        raise Exception()
    
def render_media_builder():
    try:
        MEDIA_BUILDER_ID = get_input("media builder id", True)
        
        nomad_sdk.render_media_builder(MEDIA_BUILDER_ID)
    except:
        raise Exception()
    
def update_media_builder():
    try:
        MEDIA_BUILDER_ID = get_input("media builder id", True)
        NAME = get_input("name", False)
        DESTINATION_FOLDER_ID = get_input("destination folder id", False)
        COLLECTIONS = get_input("collections", False)
        RELATED_CONTENTS = get_input("related contents", False)
        TAGS = get_input("tags", False)
        PROPERTIES = get_input("properties", False)

        MEDIA_BUILD = nomad_sdk.update_media_builder(MEDIA_BUILDER_ID, NAME, DESTINATION_FOLDER_ID,
            COLLECTIONS, RELATED_CONTENTS, TAGS, PROPERTIES)
        
        print(json.dumps(MEDIA_BUILD, indent=4))
    except:
        raise Exception()
    
def get_media_builder_ids_from_asset():
    try:
        SOURCE_ASSET_ID = get_input("source asset id", True)

        MEDIA_BUILDER_IDS = nomad_sdk.get_media_builder_ids_from_asset(SOURCE_ASSET_ID)

        print(json.dumps(MEDIA_BUILDER_IDS, indent=4))
    except:
        raise Exception()

    
FUNCTIONS = {
    "1": create_media_builder,
    "2": create_media_builder_item,
    "3": create_media_builder_items_add_annotations,
    "4": create_media_builder_items_bulk,
    "5": delete_media_builder,
    "6": delete_media_builder_item,
    "7": duplicate_media_builder,
    "8": get_media_builder,
    "9": get_media_builders,
    "10": get_media_builder_items,
    "11": move_media_builder_item,
    "12": render_media_builder,
    "13": update_media_builder,
    "14": get_media_builder_ids_from_asset
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