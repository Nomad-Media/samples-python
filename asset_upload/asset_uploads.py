from nomad_media_pip.nomad_sdk import Nomad_SDK
from config import config

nomad_sdk = Nomad_SDK(config)

import json

def upload_asset():
    try:
        NAME = input("Enter asset name (press enter if you want name of file to be name): ")
    
        EXISTING_ASSET_ID = input("Enter existing asset id: ") if input("Do you want to add an existing asset id (y/n): ") == "y" else ""
        RELATED_ASSET_ID = input("Enter related asset id: ") if input("Do you want to add a related asset id (y/n): ") == "y" else ""
        LANGUAGE_ID = input("Enter language id: ") if input("Do you want to add a language id (y/n): ") == "y" else ""
        PARENT_ID = input("Enter parent id: ") if input("Do you want to add a parent id (y/n): ") == "y" else ""
    
        while True:
            UPLOAD_OVERWRITE_OPTION = input("Enter upload overwrite option (replace, continue, cancel): ")
            if UPLOAD_OVERWRITE_OPTION == "replace" or UPLOAD_OVERWRITE_OPTION == "continue" \
            or UPLOAD_OVERWRITE_OPTION == "cancel":
                break
            print("Invalid input")
        FILE = input("Enter file path: ")
        RELATED_CONTENT_ID = input("Enter related content id (press enter to skip): ")
    
        ASSET_INFO = nomad_sdk.upload_asset(NAME, EXISTING_ASSET_ID, RELATED_ASSET_ID,
                                            RELATED_CONTENT_ID, LANGUAGE_ID, 
                                            UPLOAD_OVERWRITE_OPTION, FILE, PARENT_ID)
    
        print(json.dumps(ASSET_INFO, indent=4))
    except Exception as e:
        print(e)

def upload_related_asset():
    try:
        EXISTING_ASSET_ID = input("Enter existing asset id: ")
        RELATED_ASSET_ID = input("Enter related asset id: ") if input("Do you want to add a related asset id (y/n): ") == "y" else None
        NEW_RELATED_ASSET_METADATA_TYPE = input("Enter new related asset metadata type: ")
        FILE = input("Enter file path: ")
        LANGUAGE_ID = input("Enter language id: ") if input("Do you want to add a language id (y/n): ") == "y" else None

        while True:
            UPLOAD_OVERWRITE_OPTION = input("Enter upload overwrite option (replace, continue, cancel): ")
            if UPLOAD_OVERWRITE_OPTION == "replace" or UPLOAD_OVERWRITE_OPTION == "continue" \
            or UPLOAD_OVERWRITE_OPTION == "cancel":
                break
            print("Invalid input")

        ASSET_INFO = nomad_sdk.upload_related_asset(EXISTING_ASSET_ID, RELATED_ASSET_ID, NEW_RELATED_ASSET_METADATA_TYPE, UPLOAD_OVERWRITE_OPTION, FILE, LANGUAGE_ID)

        print(json.dumps(ASSET_INFO, indent=4))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    upload_asset()
