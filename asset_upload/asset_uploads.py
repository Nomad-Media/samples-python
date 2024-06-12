from nomad_media_pip.src.nomad_sdk import Nomad_SDK
from config import config

nomad_sdk = Nomad_SDK(config)

import json

def upload_asset():
    try:
        NAME = input("Enter asset name: ") if input("Do you want to add an asset name (y/n): ") == "y" else ""
        EXISTING_ASSET_ID = input("Enter existing asset id: ") if input("Do you want to add an existing asset id (y/n): ") == "y" else ""
        RELATED_CONTENT_ID = input("Enter related content id: ") if input("Do you want to add a related content id (y/n): ") == "y" else None
    
        while True:
            UPLOAD_OVERWRITE_OPTION = input("Enter upload overwrite option (replace, continue, cancel): ")
            if UPLOAD_OVERWRITE_OPTION == "replace" or UPLOAD_OVERWRITE_OPTION == "continue" \
            or UPLOAD_OVERWRITE_OPTION == "cancel":
                break
            print("Invalid input")
        FILE = input("Enter file path: ")
        PARENT_ID = input("Enter parent id: ") if input("Do you want to add a parent id (y/n): ") == "y" else ""
        LANGUAGE_ID = input("Enter language id: ") if input("Do you want to add a language id (y/n): ") == "y" else ""
    
        ASSET_INFO = nomad_sdk.upload_asset(NAME, EXISTING_ASSET_ID, RELATED_CONTENT_ID,
                                            UPLOAD_OVERWRITE_OPTION, FILE, PARENT_ID, LANGUAGE_ID)
    
        print(json.dumps(ASSET_INFO, indent=4))
    except Exception as e:
        print(e)

def upload_related_asset():
    try:
        EXISTING_ASSET_ID = input("Enter existing asset id: ")
        RELATED_ASSET_ID = input("Enter related asset id: ") if input("Do you want to add a related asset id (y/n): ") == "y" else None
        NEW_RELATED_ASSET_METADATA_TYPE = input("Enter new related asset metadata type: ")

        while True:
            UPLOAD_OVERWRITE_OPTION = input("Enter upload overwrite option (replace, continue, cancel): ")
            if UPLOAD_OVERWRITE_OPTION == "replace" or UPLOAD_OVERWRITE_OPTION == "continue" \
            or UPLOAD_OVERWRITE_OPTION == "cancel":
                break
            print("Invalid input")
        FILE = input("Enter file path: ")
        LANGUAGE_ID = input("Enter language id: ") if input("Do you want to add a language id (y/n): ") == "y" else None

        ASSET_INFO = nomad_sdk.upload_related_asset(EXISTING_ASSET_ID, RELATED_ASSET_ID, NEW_RELATED_ASSET_METADATA_TYPE, 
                                                    UPLOAD_OVERWRITE_OPTION, FILE, LANGUAGE_ID)

        print(json.dumps(ASSET_INFO, indent=4))
    except Exception as e:
        print(e)

functions = {
    "1": upload_asset,
    "2": upload_related_asset
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
