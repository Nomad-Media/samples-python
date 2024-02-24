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

        CONTENT_ID = get_input("content id", True) if input("Do you want to create a new event (y/n): ") == "n" else None
        START_DATETIME = get_input("start datetime (YYYY-MM-DDTHH:MM:SS)", True)
        END_DATETIME = get_input("end datetime (YYYY-MM-DDTHH:MM:SS)", True)
        EVENT_TYPE = get_dict("event type", ["id", "description"], True)
        SERIES = get_dict("series", ["id", "description"], False)
        IS_DISABLED = get_bool("is disabled")
        OVERRIDE_SERIES_PROPERTIES = get_bool("override series properties")

        SERIES_PROPERTIES = {}
        if OVERRIDE_SERIES_PROPERTIES or SERIES == {}:
            NAME = get_input("name", True)
            while True:
                if input("Do you want to add additional properties (y/n): ") == "n":
                    break
                else:
                    key = input("Enter additional property key: ")
                    value = input("Enter additional property value: ")
                    SERIES_PROPERTIES[key] = value
        else:
            NAME = None
            SERIES_PROPERTIES = None

        INFO = nomad_sdk.create_and_update_event(CONTENT_ID, EVENT_CONTENT_DEFINITION_ID,
                                                 NAME, START_DATETIME, END_DATETIME, EVENT_TYPE, 
                                                 SERIES, IS_DISABLED, OVERRIDE_SERIES_PROPERTIES, 
                                                 SERIES_PROPERTIES)
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
