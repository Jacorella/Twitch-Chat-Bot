# Twitch Chat Bot

This is a Python project that utilizes the TwitchIO library to create a chat bot for Twitch. The bot is able to connect to a Twitch channel specified by the user and display chat messages in a Tkinter window. Additionally, this bot contains few twitch emojis

## Requirements

- Python 3.6 or later
- TwitchIO library (can be installed via pip):  pip install twitchio
- Tkinter library (already included in Python versions)

## How to use the bot

1. Clone or download the repository.
2. Open the terminal in the directory where the `twitch_chat_bot.py` file is located.
3. Install the TwitchIO library by typing the following command: pip install twitchio
4. Open the `twitch_chat_bot.py` file in a text editor.
5. Insert your OAuth token, Twitch channel username, and custom emojis into the code.
6. Save the file and close the text editor.
7. Type the following command to start the bot:

```
python twitch_chat_bot.py
```

The Tkinter window containing the Twitch chat for the specified channel will be launched.
Interact with the bot in the Tkinter chat window.
Note: please keep in mind that using this bot may violate Twitch's Terms of Service. Use it at your own risk. Also, note that using this bot may cause an increase in chat traffic in the Twitch channel, which may affect the quality of service for other users.

Customization
The bot can be customized in various ways, including:

Adding custom commands using the TwitchIO library
Changing the command prefix (currently set to "!")
Adding custom emojis to the EMOJI_DICT dictionary
License
This project is released under the MIT License. See the LICENSE file for more information.

Authors
Jacorella - Main author
Acknowledgments
TwitchIO - Library used to connect to Twitch and interact with the chat.
Tkinter - Library used to create the chat user interface.
Pillow - Library used to manipulate emoji images.
