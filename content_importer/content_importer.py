from nomad_media_pip.src.nomad_sdk import Nomad_SDK
from config import config

import uuid, os

nomad_sdk = Nomad_SDK(config)

def check_contents(CONTENTS, CONTENT_DEFINITION_NAME):
    CONTENT_DEFINITIONS = nomad_sdk.get_content_definitions(None, None, None, None, None)
    CONTENT_DEFINITION = next((definition for definition in CONTENT_DEFINITIONS["items"] if definition["properties"]["title"] == CONTENT_DEFINITION_NAME), None)

    if not CONTENT_DEFINITION:
        CONTENT_DEFINITION = nomad_sdk.create_content_definition()
        CONTENT_DEFINITION_ID = CONTENT_DEFINITION["contentDefinitionId"]

        CONTENT_FIELDS = [
            {
                "contentFieldId": str(uuid.uuid4()),
                "listViewSequence": 1,
                "editorViewSequence": 1,
                "isInEditorForm": True,
                "isInContentList": True,
                "isDeleted": False,
                "isSystemField": False,
                "properties": {
                    "isIndexIdentifier": True,
                    "shortTextProperties": {
                        "textType": 1,
                        "textTypeLabel": "Text"
                    },
                    "title": "Name",
                    "propertyName": "Name",
                    "fieldId": {
                        "description": "Short Text",
                        "id": "ea652681-fc45-4cba-8a7e-e13350d62522"
                    },
                    "isRequired": True
                }
            }
        ]

        nomad_sdk.update_content_definition(CONTENT_DEFINITION_ID, CONTENT_DEFINITION_NAME, 
            CONTENT_FIELDS, "Custom Definitions", "Basic Content Type", "Name", None, None, None, True, True)
        
        CONTENT_DEFINITION_CONTENTS = None
    else:
        CONTENT_DEFINITION_ID = CONTENT_DEFINITION["contentDefinitionId"]

        CONTENT_DEFINITION_CONTENTS = []
        offset = 0
        while True:
            SEARCH_INFO = nomad_sdk.search(None, offset, None, [
                {
                    "fieldName": "contentDefinitionId",
                    "operator": "equals",
                    "values": CONTENT_DEFINITION_ID
                }
            ], None, None, None, None, True, None)

            CONTENT_DEFINITION_CONTENTS += SEARCH_INFO["items"]

            if len(CONTENTS) < 100:
                break

            offset += 1

    CONTENT_DEFINITION_CONTENT_NAMES = [content["identifiers"]["name"] for content in CONTENT_DEFINITION_CONTENTS] if CONTENT_DEFINITION_CONTENTS else []

    for content in CONTENTS:
        if content not in CONTENT_DEFINITION_CONTENT_NAMES and content != "":
            CONTENT = nomad_sdk.create_content(CONTENT_DEFINITION_ID, None)
            CONTENT_ID = CONTENT["contentId"]

            print(f"Adding {content}")
            nomad_sdk.update_content(CONTENT_ID, CONTENT_DEFINITION_ID, { "name": content }, None)

            CONTENT_DEFINITION_CONTENT_NAMES.append(content)
        

def get_contents(file, delimiter):
    with open(file, 'r') as f:
        return f.read().split(delimiter)

if __name__ == "__main__":
    FILE_PATH = input("Enter the file path: ")
    DELIMITER = input("Enter the delimiter: ")
    CONTENTS = get_contents(FILE_PATH, '\n')

    FILE_NAME = os.path.basename(FILE_PATH)
    CONTENT_DEFINITION_NAME = FILE_NAME.split(".")[0].capitalize()
    check_contents(CONTENTS, CONTENT_DEFINITION_NAME)

    print("Contents have been added")