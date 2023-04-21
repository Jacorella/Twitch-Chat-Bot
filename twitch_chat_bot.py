import random
import sys
import re
import asyncio
from twitchio.ext import commands
import tkinter as tk
from tkinter import scrolledtext
import threading
from PIL import Image, ImageTk  


# Inserisci il tuo token, nome utente e canale di Twitch qui
TWITCH_TOKEN = 'oauth:tlfztec764cgqx37tcricxn1jtk6w9'
TWITCH_CHANNEL = input("Insert the name of the Streamer: ")

# Aggiungi un dizionario per memorizzare le emoji
EMOJI_DICT = {
    'BibleThump': 'emojis/BibleThump.png',
    'KEKW': 'emojis/KEKW.png',
}


class TwitchChatBot(commands.Bot):

    def __init__(self, update_gui):
        super().__init__(token=TWITCH_TOKEN, prefix='!', initial_channels=[TWITCH_CHANNEL])
        self.update_gui = update_gui

    async def event_ready(self):
        print("The Bot is ready!")

    async def event_message(self, message):
        if message.echo or message.author.name == self.nick:
            return

        print(f'{message.author.name}: {message.content}')
        self.update_gui(message.author.name, message.content)


class TwitchBotThread(threading.Thread):

    def __init__(self, window, update_gui, *args, **kwargs):
        super(TwitchBotThread, self).__init__(*args, **kwargs)
        self.window = window
        self.update_gui = update_gui

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        bot = TwitchChatBot(self.update_gui)
        loop.run_until_complete(bot.start())

        loop.close()


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.user_colors = {}
        self.chat_box.image_list = []

    def init_ui(self):
        self.title('Twitch Chat')
        self.geometry('400x600')

        # Imposta l'icona della finestra utilizzando un file PNG
        self.icon_image = tk.PhotoImage(file='logo.png')
        self.iconphoto(False, self.icon_image)

        self.chat_box = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=('Arial', 12), bg='#333', fg='#fff', padx=10, pady=10)
        self.chat_box.pack(expand=True, fill=tk.BOTH)
        self.chat_box.configure(state='disabled')

        self.configure(bg='#222')

    def update_chat(self, username, message):
        user_color = self.get_user_color(username)

        # Create a tag for the username with the associated color
        tag_name = f'tag_{username}'
        self.chat_box.tag_configure(tag_name, foreground=user_color)

        self.chat_box.configure(state='normal')
        self.chat_box.insert(tk.END, f'{username}: ', tag_name)

        # Aggiungi il supporto per le emoji
        split_message = re.split(r'(\W+)', message)
        for word in split_message:
            if word in EMOJI_DICT:
                emoji_path = EMOJI_DICT[word]
                emoji_image = Image.open(emoji_path)
                emoji_image.thumbnail((20, 20))  # Ridimensiona l'emoji

                # Converti l'emoji in formato PhotoImage
                emoji_photo = ImageTk.PhotoImage(emoji_image)

                # Inserisci l'emoji nella casella di chat
                self.chat_box.image_create(tk.END, image=emoji_photo)
                self.chat_box.image_list.append(emoji_photo)  # Memorizza un riferimento all'immagine
            else:
                self.chat_box.insert(tk.END, word)

        self.chat_box.insert(tk.END, '\n')
        self.chat_box.configure(state='disabled')
        self.chat_box.see(tk.END)

    def get_user_color(self, username):
        if username in self.user_colors:
            return self.user_colors[username]
        else:
            color = self.generate_random_color()
            self.user_colors[username] = color
            return color

    def generate_random_color(self):
        r = lambda: random.randint(0, 255)
        return f'#{r():02x}{r():02x}{r():02x}'


if __name__ == '__main__':
    app = MainWindow()

    def update_gui(username, message):
        app.update_chat(username, message)

    bot_thread = TwitchBotThread(app, update_gui)
    bot_thread.daemon = True
    bot_thread.start()

    app.mainloop()