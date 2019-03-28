#!/usr/bin/env python3
from dotenv import load_dotenv, find_dotenv
from pyrogram import Client, Filters, MessageHandler
import os
import optparse
load_dotenv(find_dotenv())

PROJECT_DIRECTORY = os.path.split(os.path.realpath(__file__))[0]

app = Client(
    "my_account",
    api_id=os.getenv("MTPROTO_API_ID"),
    api_hash=os.getenv("MTPROTO_API_HASH")
)


@app.on_message(Filters.command(["start", "help"]))
def start_command(client, message):
    print(message)

@app.on_message(Filters.command(["newchat"]))
def new_chat(client, message):
    print(message)
    if message.text != None and message.text.startswith("/newchat"):
        message.reply(f'Chat name: \'{message.text.lstrip("/newchat").strip()}\'', quote=True)
        

app.run()
