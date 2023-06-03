import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
       await message.channel.send('I am dumb')

bot.run('MTExNDU1NzY1MzM3NzYzMDM1OQ.G9Slx0.cnh6Wb5WiqHXDYBQkoopZI2hkCNvXnVfaGJoCI')
