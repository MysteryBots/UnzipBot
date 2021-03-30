import os


class Config:
    API_ID = int(os.environ.get("API_ID", 0))  # Change 12345 to your API_ID
    API_HASH = os.environ.get("API_HASH", None)  # Change None to your API_HASH
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)  # Change None to your BOT_TOKEN
    OWNER_ID = int(os.environ.get("OWNER_ID", 0))  # Change 0 to your OWNER_ID
    OWNER_NAME = os.environ.get("OWNER_NAME", None)  # Change None to your OWNER_NAME

    # For Local Deploys edit above 5 lines.
    # Put your API_ID and OWNER_ID (without comma) and API_HASH,BOT_TOKEN n OWNER_NAME (with commas) below.
    # If got any problem ask in @MysteryBotsChat.