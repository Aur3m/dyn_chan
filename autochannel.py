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
    
@bot.command(name="help")
async def help(ctx, extension):
    #print "help" text
    
@bot.command(name="create")
async def help(ctx, extension):
    #verify if the user using the command has the admin permission
   
def create_new_channel(id):
    #create a new channel with the same permissions in the same category with "[NAME] #[NUMBER]+1"

def rename_current_channel(id):
    #rename a channel with "[NAME] #[NUMBER]-1"

def remove_channel(id):
    #remove, delete the concerned channel

