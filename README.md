# bot-logger
Simple discord bot, that can log all your messages on the server

[README на русском тут](https://github.com/atarwn/bot-logger/blob/main/RU-README.MD)
## How it works
The bot reads the message, its author, and the channel on which it was sent. Then, it saves it to the `log.txt` file like "author@channel: message"

p.s. Make sure that you invite the bot to the right server, and make sure that only you can add this bot, because the bot is optimized to work with only one server.

p.s.s. PLEASE make sure you have Python and the discord library installed
## How to set up
### Windows or any other system with GUI
1. Download file [bot.py](https://github.com/atarwn/bot-logger/blob/main/bot.py)
2. Open file by any editor
3. Replace the "WRITE_TOKEN_HERE" by your bot token
4. Run it
### Linux Terminal
1. `git clone https://github.com/atarwn/bot-logger`
2. `cd bot-logger`
3. `vim bot.py` # Or use any other code editor
4. `i` # Edit file
5. Replace the "WRITE_TOKEN_HERE" by your bot token
6. `:wq` # Saves the file and exits Vim
7. `python bot.py`
### Other systems
Same or similar to setting up a bot in Windows or Linux terminal
## Installing python and discord library
### Windows
1. Go to [python.org](https://python.org) website and download Python
2. Follow the installer's instructions
3. Press Win+R and type `cmd`
4. Windows terminal will open, write `pip install discord`
5. The preparation is complete! Now follow the instructions to install and configuring the bot
### Linux Terminal
1. `apt install git` or `pkg install git`
2. `apt install python` or `pkg install python`
3. `pip install discord`
4. The preparation is complete! Now follow the instructions to install and configuring the bot

> `First attempt to write a normal README.md`

