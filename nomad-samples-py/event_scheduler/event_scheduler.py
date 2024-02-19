from nomad_media_pip.nomad_sdk import Nomad_SDK
from config import config

nomad_sdk = Nomad_SDK(config)

import json

EVENT_CONTENT_DEFINITION_ID = "412a30e3-73ee-4eae-b739-e1fc87601c7d"

def get_input(prompt, required):
    return input(f"Enter {prompt}: ") if required or input(f"Do you want to add {prompt} (y/n): ") == "y" else ""

def get_dict(prompt, keys, required):
    return {key: input(f"Enter {prompt} {key}: ") for key in keys} if required or input(f"Do you want to add {prompt} (y/n): ") == "y" else {}

def get_list(prompt, keys, required):
    items = []
    if required or input(f"Do you want to add {prompt} (y/n): ") == "y":
        while True:
            items.append({key: input(f"Enter {prompt} {key}: ") for key in keys})
            if not required or input(f"Do you want to add another {prompt} (y/n): ") == "n":
                break
    return items

def get_bool(prompt):
    return True if input(f"{prompt} (y/n): ") == "y" else False

def get_data(prompts):
    data = {}
    for key, value in prompts.items():
        type = value[1]
        if type == "input":
            prompt, type, required = value
            data[key] = get_input(prompt, required)
        elif type == "dict":
            prompt, keys, type, required = value
            data[key] = get_dict(prompt, keys, required)
        elif type == "list":
            prompt, keys, type, required = value
            data[key] = get_list(prompt, keys, required)
        elif type == "bool":
            prompt, type, required = value
            data[key] = get_bool(prompt)

    return data

def get_days():
    SEARCH_INFO = nomad_sdk.search(None, None, None, 
        [
            {
                "fieldName": "contentDefinitionId",
                "operator": "Equals",
                "values": "fc8042c1-1ade-400d-b0aa-02937e658ae6",
            },
            {
                "fieldName": "languageId",
                "operator": "Equals",
                "values": "c66131cd-27fc-4f83-9b89-b57575ac0ed8"
            }
        ], None, None, None, None, True, None)
    
    print(json.dumps(SEARCH_INFO, indent=4))

    return SEARCH_INFO["items"]

def create_and_update_event():
    try:
        prompts = {
            "CONTENT_ID": ("content id (enter y for updating event)", "input", False),
            "CONTENT_DEFINITION_ID": EVENT_CONTENT_DEFINITION_ID,
            "NAME": ("event name", "input", True),
            "SERIES": ("series", "dict", ["id", "description"], False),
            "START_DATETIME": ("start datetime (YYYY-MM-DD HH:MM:SS)", "input", True),
            "END_DATETIME": ("end datetime (YYYY-MM-DD HH:MM:SS)", "input", True),
            "PRIMARY_PERFORMER": ("primary performer", "dict", ["id", "description"], False),
            "SHORT_DESCRIPTION": ("short description", "input", False),
            "LONG_DESCRIPTION": ("long description", "input", False),
            "THUMBNAIL_IMAGE": ("thumbnail image", "dict", ["id", "description"], False),
            "HERO_IMAGE": ("hero image", "dict", ["id", "description"], False),
            "LOGO_IMAGE": ("logo image", "dict", ["id", "description"], False),
            "INTELLIGENT_PROGRAMMING": ("intelligent programming", "dict", ["id", "description"], False),
            "EXTERNAL_URL": ("external url", "input", False),
            "VENUE": ("venue", "dict", ["id", "description"], False),
            "PERFORMERS": ("performer", "list", ["id", "description"], False),
            "GENRES": ("genre", "list", ["id", "description"], False),
            "MEDIA_ATTRIBUTES": ("media attribute", "list", ["id", "description"], False),
            "LANGUAGES": ("language", "list", ["id", "description"], False),
            "PRODUCTS": ("product", "list", ["id", "description"], False),
            "FEATURE_GROUPS": ("feature group", "list", ["id", "description"], False),
            "GROUP_SEQUENCE": ("group sequence", "input", False),
            "RELATED_MEDIA_ITEMS": ("related media item", "list", ["id", "description"], False),
            "RECOMMENDATION_SIMMILAR_ITEMS": ("recommendation similar item", "list", ["id", "description"], False),
            "CONTENT_RATINGS": ("content rating", "list", ["id", "description"], False),
            "IS_DISABLED": ("disable the event", "bool"),
            "LIVE_CHANNEL": ("live channel", "dict", ["id", "description"], False)
        }

        data = get_data(prompts)

        INFO = nomad_sdk.create_and_update_event(**data)
        print(json.dumps(INFO, indent=4))
    except:
        raise Exception()
    
def add_live_schedule_to_event():
    try:
        prompts = {
            "EVENT_ID": ("event id", "input", True),
            "SLATE_VIDEO": ("slate video", "dict", ["id", "description"], False),
            "PREROLL_VIDEO": ("preroll video", "dict", ["id", "description"], False),
            "POSTROLL_VIDEO": ("postroll video", "dict", ["id", "description"], False),
            "IS_SECURE_OUTPUT": ("secure output", "bool"),
            "ARCHIVE_FOLDER": ("archive folder", "dict", ["id", "description"], False),
            "PRIMARY_LIVE_INPUT": ("primary live input", "dict", ["id", "description"], False),
            "BACKUP_LIVE_INPUT": ("backup live input", "dict", ["id", "description"], False),
            "PRIMARY_LIVE_INPUT_URL": ("primary live input url", "input", False),
            "BACKUP_LIVE_INPUT_URL": ("backup live input url", "input", False),
            "EXTERNAL_OUTPUT_PROFILES": ("external output profile ", "list", ["id", "description"], False)
        }

        data = get_data(prompts)

        INFO = nomad_sdk.add_live_schedule_to_event(**data)
        print(json.dumps(INFO, indent=4))
    except:
        raise Exception()
    
def extend_live_schedule():
    try:
        prompts = {
            "EVENT_ID": ("event id", "input", True),
            "RECURRING_DAYS": ("the days you want the event to recur on (separate by comma)", "input", True),
            "RECURRING_WEEKS": ("the number of weeks you want the event to recur on", "input", True),
            "END_DATE": ("the end date of the event (YYYY-MM-DD)", "input", False),
        }

        data = get_data(prompts)

        data["RECURRING_DAYS"] = [day for day in get_days() if day["title"] in data["RECURRING_DAYS"]]

        INFO = nomad_sdk.extend_live_schedule(**data)
        print(json.dumps(INFO, indent=4))
    except:
        raise Exception()

def get_live_schedule():
    try:
        prompts = {
            "EVENT_ID": ("event id", "input", True),
        }

        data = {}
        for key, value in prompts.items():
            prompt, type, required = value
            data[key] = get_input(prompt, required)

        print("Getting live schedule")
        INFO = nomad_sdk.get_live_schedule(**data)
        print(json.dumps(INFO, indent=4))
    except:
        raise Exception()
    
def start_live_schedule():
    try:
        prompts = {
            "EVENT_ID": ("event id", "input", True),
        }

        data = {}
        for key, value in prompts.items():
            prompt, type, required = value
            data[key] = get_input(prompt, required)

        INFO = nomad_sdk.start_live_schedule(**data)
        print(json.dumps(INFO, indent=4))
    except:
        raise Exception()
    
def stop_live_schedule():
    try:
        prompts = {
            "EVENT_ID": ("event id", "input", True),
        }

        data = {}
        for key, value in prompts.items():
            prompt, type, required = value
            data[key] = get_input(prompt, required)

        INFO = nomad_sdk.stop_live_schedule(**data)
        print(json.dumps(INFO, indent=4))
    except:
        raise Exception()
    
def delete_live_schedule():
    try:
        prompts = {
            "CONTENT_ID": ("event id", "input", True),
            "CONTENT_DEFINITION_ID": EVENT_CONTENT_DEFINITION_ID
        }

        data = {}
        for key, value in prompts.items():
            prompt, type, required = value
            data[key] = get_input(prompt, required)

        INFO = nomad_sdk.delete_content(**data)
        print(json.dumps(INFO, indent=4))
    except:
        raise Exception()
    
functions = {
    "1": create_and_update_event,
    "2": add_live_schedule_to_event,
    "3": extend_live_schedule,
    "4": get_live_schedule,
    "5": start_live_schedule,
    "6": stop_live_schedule,
    "7": delete_live_schedule,
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
