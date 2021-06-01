import discord
import os
from discord.ext import commands
token = ''

client = discord.Client()

intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="c!",intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="c!help for more information"))
   
   bot.run(token)
   
def create_new_channel(id):

def rename_current_channel(id):

def remove_channel(id):

