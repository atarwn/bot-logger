import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='1', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print("Бот активен")
    try:
        open('log.txt', 'a')
    except:
        open('log.txt', 'w').write('New log file created\n\n')

@bot.event
async def on_message(ctx):
    log = open('log.txt', 'a')
    log.write(f"{ctx.author}@{ctx.channel.name}: {ctx.content}\n")
    print(f"{ctx.author}@{ctx.channel.name}: {ctx.content}")
    log.close

bot.run("WRITE_YOUR_TOKEN")
