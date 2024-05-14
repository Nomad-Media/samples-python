from nomad_media_pip.nomad_sdk import Nomad_SDK
from config import config

nomad_sdk = Nomad_SDK(config)

def get_input(prompt, required):
    return input(f"Enter {prompt}: ") if required or input(f"Do you want to add {prompt} (y/n): ") == "y" else None

def get_dict(prompt, keys, required):
    return {key: input(f"Enter {prompt} {key}: ") for key in keys} if required or input(f"Do you want to add {prompt} (y/n): ") == "y" else None

def get_list(prompt, keys, required):
    items = []
    if required or input(f"Do you want to add a {prompt} (y/n): ") == "y":
        while True:
            items.append({key: input(f"Enter {prompt} {key}: ") for key in keys})
            if input(f"Do you want to add another {prompt} (y/n): ") == "n":
                break
    return items

def asset_external_upload():
    try:
        ASSET_NAME = get_input("asset name", True)
        PARENT_DIR_ID = get_input("parent directory id", True)
        FILE_PATH = get_input("file path", True)
        TAGS = get_list("tag", ["id"], False)
        LANGUAGE = get_dict("language", ["id"], False)

        LANGUAGE_ID = LANGUAGE["id"] if LANGUAGE else None

        PLACEHOLDER_INFO = nomad_sdk.create_placeholder_asset(PARENT_DIR_ID, ASSET_NAME)

        nomad_sdk.upload_asset(ASSET_NAME, PLACEHOLDER_INFO["id"], None, "replace", 
                               FILE_PATH, PARENT_DIR_ID, LANGUAGE_ID)
        
        nomad_sdk.bulk_update_metadata([PLACEHOLDER_INFO["id"]], None, None, [item["id"] for item in TAGS], None)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asset_external_upload()