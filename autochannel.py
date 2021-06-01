import discord
import os
from discord.ext import commands

token = ''

client = discord.Client()

intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)


def foo():
    pass


bot = commands.Bot(command_prefix="c!", intents=intents, help_command=foo())


@bot.event
async def on_ready():
    print("loaded")
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="c!help for more information"))


@bot.command(name="help")
async def help(ctx):
    embed=discord.Embed(title="Current Prefix ", description="c!")
    embed.set_author(name="Usage")
    embed.set_thumbnail(url="https://i.imgur.com/GKadtia.png")
    embed.add_field(name="create_autochannel", value="[Admin Only] You need to go in a voice channel and process with this command to make this channel automatic", inline=True)
    embed.add_field(name="remove_autochannel [ID]", value="[Admin Only] Remove an autochannel using its specific ID", inline=True)
    embed.add_field(name="list", value="List all the current autochannels of your server and their ID(s)", inline=True)
    await ctx.send(embed=embed)


# print "help" text

@bot.command(name="create")
async def create(ctx):


# verify if the user using the command has the admin permission
# create a .json with the server id and assign an id to this new autochannel

@bot.command(name="remove")
async def remove(ctx, id):


# remove one of the numerous autochannels defined for the server

@bot.command(name="list")
async def list(ctx):


# parse the current active autochannels and their ids from the concerned .json of the current server

def create_new_channel(id):
    


# create a new channel with the same permissions in the same category with "[NAME] #[NUMBER]+1"

def rename_current_channel(id):


# rename a channel with "[NAME] #[NUMBER]-1"

def remove_channel(id):


# remove, delete the concerned channel

def init_autochannel():
    
def remove_autochannel():

bot.run(token)
