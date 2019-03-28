# mediator
Mediates group chats.

## Requirements
- Python 3.5+
- Linux/macOS environment
- A Telegram user account (can be separate from your primary account)

## Running an instance
- `git clone https://github.com/au5ton/mediator.git`
- `pip3 install -r requirements.txt`
- [Register a new Telegram application](https://my.telegram.org/apps)
- `cp .env.example .env`
- Supply API ID and API Hash that was provided when registering your Telegram application by editing the `.env` file
- Run the python script: `python3 bot.py`
- Follow instructions to sign into a Telegram user account
- The bot is now running

## What is a userbot?
Although rare, a Telegram userbot is a type of Telegram bot that does not run from a Telegram bot account, but from a full user account. Telegram userbots are fully-fledged Telegram accounts. The only reason a Telegram bot would be made to be a userbot instead of a normal bot created by the BotFather is because of API limitations. 

## Why is gifvbot a userbot instead of a normal bot?
mediator is a userbot because the Telegram bot API [does not allow bots to create groups](https://core.telegram.org/bots/api#file), which is necessary for mediator's solution. The only solution was to make mediator a userbot.
