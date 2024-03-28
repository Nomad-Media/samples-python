from nomad_media_pip.nomad_sdk import Nomad_SDK
from config import config

nomad_sdk = Nomad_SDK(config)

import json

def get_live_output_profiles():
    profiles = nomad_sdk.get_live_output_profiles()
    print(json.dumps(profiles, indent=4))

def get_live_output_profile():
    OUTPUT_ID = input("Enter the output ID: ")

    RESULT = nomad_sdk.get_live_output_profile(OUTPUT_ID)
    print(json.dumps(RESULT, indent=4))

def get_live_output_types():
    types = nomad_sdk.get_live_output_types()
    print(json.dumps(types, indent=4))

def create_live_output_profile():
    OUTPUT_TYPES = nomad_sdk.get_live_output_types()

    NAME = input("Enter the name of the new profile: ")
    OUTPUT_TYPE_DESCRIPTION = input(f"Enter the output type: {', '.join([OUTPUT_TYPE['description'] for OUTPUT_TYPE in OUTPUT_TYPES])}: ") if input("Do you want to use the default output type? (y/n): ") == "n" else None
    ENABLED = input("Do you want to enable the profile? (y/n): ") == "y"
    AUDIO_BITRATE = float(input("Enter the audio bitrate: ")) if input("Do you want to enter an audio bitrate (y/n): ") == "y" else None
    OUTPUT_STREAM_KEY = input("Enter the output stream key: ") if input("Do you want to enter an output stream key? (y/n): ") == "y" else None
    OUTPUT_URL = input("Enter the output URL: ") if input("Do you want to enter an output URL? (y/n): ") == "y" else None
    SECONDARY_OUTPUT_STREAM_KEY = input("Enter the secondary output stream key: ") if input("Do you want to enter a secondary output stream key? (y/n): ") == "y" else None
    SECONDARY_OUTPUT_URL = input("Enter the secondary output URL: ") if input("Do you want to enter a secondary output URL? (y/n): ") == "y" else None
    VIDEO_BITRATE = float(input("Enter the video bitrate: ")) if input("Do you want to enter a video bitrate? (y/n): ") == "y" else None
    VIDEO_BITRATE_MODE = input("Enter the video bitrate mode: (CBR or VBR)") if input("Do you want to enter a video bitrate mode? (y/n): ") == "y" else None
    VIDEO_CODEC = input("Enter the video codec: (H264 or H265)") if input("Do you want to enter a video codec? (y/n): ") == "y" else None
    VIDEO_FRAMES_PER_SECOND = float(input("Enter the video frames per second: ")) if input("Do you want to enter the video frames per second? (y/n): ") == "y" else None
    VIDEO_HEIGHT = float(input("Enter the video height: ")) if input("Do you want to enter the video height? (y/n): ") == "y" else None
    VIDEO_WIDTH = float(input("Enter the video width: ")) if input("Do you want to enter the video width? (y/n): ") == "y" else None

    OUTPUT_TYPE = next((OUTPUT_TYPE for OUTPUT_TYPE in OUTPUT_TYPES if OUTPUT_TYPE['description'] == OUTPUT_TYPE_DESCRIPTION), None)

    RESULT = nomad_sdk.create_live_output_profile(NAME, OUTPUT_TYPE, ENABLED, AUDIO_BITRATE,
        OUTPUT_STREAM_KEY, OUTPUT_URL, SECONDARY_OUTPUT_STREAM_KEY, SECONDARY_OUTPUT_URL, 
        VIDEO_BITRATE, VIDEO_BITRATE_MODE, VIDEO_CODEC, VIDEO_FRAMES_PER_SECOND, 
        VIDEO_HEIGHT, VIDEO_WIDTH)
    
    print(json.dumps(RESULT, indent=4))

def update_live_output_profile():
    OUTPUT_TYPES = nomad_sdk.get_live_output_types()

    OUTPUT_ID = input("Enter the output ID: ")
    NAME = input("Enter the name of the new profile: ") if input("Do you want to update the name? (y/n): ") == "y" else None
    OUTPUT_TYPE_DESCRIPTION = input(f"Enter the output type: {', '.join([OUTPUT_TYPE['description'] for OUTPUT_TYPE in OUTPUT_TYPES])}: ") if input("Do you want to use the default output type? (y/n): ") == "n" else None
    ENABLED = input("Do you want to enable the profile? (y/n): ") == "y" 
    AUDIO_BITRATE = float(input("Enter the audio bitrate: ")) if input("Do you want to enter an audio bitrate (y/n): ") == "y" else None
    OUTPUT_STREAM_KEY = input("Enter the output stream key: ") if input("Do you want to enter an output stream key? (y/n): ") == "y" else None
    OUTPUT_URL = input("Enter the output URL: ") if input("Do you want to enter an output URL? (y/n): ") == "y" else None
    SECONDARY_OUTPUT_STREAM_KEY = input("Enter the secondary output stream key: ") if input("Do you want to enter a secondary output stream key? (y/n): ") == "y" else None
    SECONDARY_OUTPUT_URL = input("Enter the secondary output URL: ") if input("Do you want to enter a secondary output URL? (y/n): ") == "y" else None
    VIDEO_BITRATE = float(input("Enter the video bitrate: ")) if input("Do you want to enter a video bitrate? (y/n): ") == "y" else None
    VIDEO_BITRATE_MODE = input("Enter the video bitrate mode: (CBR or VBR)") if input("Do you want to enter a video bitrate mode? (y/n): ") == "y" else None
    VIDEO_CODEC = input("Enter the video codec: (H264 or H265)") if input("Do you want to enter a video codec? (y/n): ") == "y" else None
    VIDEO_FRAMES_PER_SECOND = float(input("Enter the video frames per second: ")) if input("Do you want to enter the video frames per second? (y/n): ") == "y" else None
    VIDEO_HEIGHT = float(input("Enter the video height: ")) if input("Do you want to enter the video height? (y/n): ") == "y" else None
    VIDEO_WIDTH = float(input("Enter the video width: ")) if input("Do you want to enter the video width? (y/n): ") == "y" else None

    OUTPUT_TYPE = next((OUTPUT_TYPE for OUTPUT_TYPE in OUTPUT_TYPES if OUTPUT_TYPE['description'] == OUTPUT_TYPE_DESCRIPTION), None)

    RESULT = nomad_sdk.update_live_output_profile(OUTPUT_ID, NAME, OUTPUT_TYPE, ENABLED, AUDIO_BITRATE,
        OUTPUT_STREAM_KEY, OUTPUT_URL, SECONDARY_OUTPUT_STREAM_KEY, SECONDARY_OUTPUT_URL, 
        VIDEO_BITRATE, VIDEO_BITRATE_MODE, VIDEO_CODEC, VIDEO_FRAMES_PER_SECOND, 
        VIDEO_HEIGHT, VIDEO_WIDTH)
    
    print(json.dumps(RESULT, indent=4))

def delete_live_output_profile():
    OUTPUT_ID = input("Enter the output ID: ")

    nomad_sdk.delete_live_output_profile(OUTPUT_ID)

functions = {
    "1": get_live_output_profiles,
    "2": get_live_output_profile,
    "3": get_live_output_types,
    "4": create_live_output_profile,
    "5": update_live_output_profile,
    "6": delete_live_output_profile
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
