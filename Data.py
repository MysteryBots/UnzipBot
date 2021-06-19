from unzipbot import app
from Config import Config
from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "Hey {}. \n\nWelcome to {} \n\nI can unzip & unrar files you send me and upload them to your private chat or to you. \nI will also total the contents & number of files."

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            START += (
                f"\n\nMy Owner :- [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neithers"
            )
            print("Quitting the bot")
            raise SystemExit
    else:
        START += f"\n\nBy @disneygrou ♥"

    # About Message
    ABOUT = "**About This Bot** \n\nThis is an Private source Unzip bot by @disneygrou \n\n👨‍🔧updates channel👨‍🔧 : [Disney Team](https://t.me/disneygrou) \n\nFramework : [Pyrogram](docs.pyrogram.org) \n\nLanguage : [Python](www.python.org) \n\nDeveloper : [Doreamonfans1](https://t.me/Doreamonfans1)"

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            ABOUT += (
                f"\n\nMy Owner :- [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neither"
            )
            print("Quitting the bot")
            raise SystemExit

    # Deploy Message
    DEPLOY = """
**Wanna create your own such bot??** 

This is made by python and this source code is private we will make the source code open and update some bugs wait until then😁
"""
    
    HELP = """
**Need Help ?? **

Send any zip/rar file then choose a mode and your work is done! 
I'll unzip/unrar it and return you it's contents.

**Available Commands** :-
/modes - Know about both modes.
/about - About this bot and source code.
/help - This Message.
/start - Check if bot is alive.

**Support** - @disneyteamchat or contact owner @doreamonfans1 
"""
    
    MODES = """
**What are Modes ❔**

1) **Tortoise 🐢**
Bit Slow but Steady. 

While using this mode you will can be notified about the all progresses happening.

Progresses include:
- downloaded so far
- contents in provided file
- number of files in provided file
- uploaded too far with number of the file being uploaded

It doesn't take too much time than other mode and is the recommended method. 

2) ** Rabbit 🐇**
Bit Fast but less user friendly.

While using this mode you won't be notified about any progresses that go on. Just download completion and upload completion will be notified. 

This is bit fast but only recommended for larger files as smaller files won't have much time difference.   
    """

    CHOOSE_MODE = "**CHOOSE MODE ** \n\nChoose a mode from below to start extracting files..."

    # Home Button
    home_button = [[InlineKeyboardButton(text="🏠 Home 🏠", callback_data="home")]]

    # Modes Buttons

    modes_buttons = [
        [
            InlineKeyboardButton("Tortoise 🐢", callback_data="tortoise"),
            InlineKeyboardButton("Rabbit 🐇", callback_data="rabbit")
        ],
        [InlineKeyboardButton("What are Modes ⁉️", callback_data="modes")]
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("What are Modes ❔", callback_data="modes"),
            InlineKeyboardButton("🤔 About🤔", callback_data="about"),
        ],
        [InlineKeyboardButton("How to Use me ❓", callback_data="help")],
        [InlineKeyboardButton("👨‍💻Developer👨‍💻", url="https://t.me/doreamonfans1")],
        [InlineKeyboardButton("👨‍🔧updates channel👨‍🔧", url="https://t.me/disneygrou")],
        [InlineKeyboardButton("🤖support group🤖", url="https://t.me/disneyteamchat")],
    ]
