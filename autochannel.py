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
    embed.add_field(name="create_autochannel", value="[Admin Only] You need to go in a voice channel and process with this command to make this channel automatic, the same permissions and category of the inital channel will be used", inline=True)
    embed.add_field(name="remove_autochannel [ID]", value="[Admin Only] Remove an autochannel using its specific ID, all channels will be deleted once all players left", inline=True)
    embed.add_field(name="list", value="List all the current autochannels of the server and their ID(s)", inline=True)
    await ctx.send(embed=embed)


# print "help" text

@bot.command(name="create")
async def create(ctx):
    print(type(ctx.author.voice.channel.name))
    #print(ctx.author.roles)
    if ctx.author.voice.channel is None or ctx.message.author.guild_permissions.administrator == False:
        return await ctx.send("You must be in a voice channel and check if you have admin permission to use this command.")


    with open(str(ctx.guild.id) + ".json", "w+", encoding="utf8") as jsonfile:
        if jsonfile.read() == "":
            jsonfile.write(json.dumps({"guild_id": ctx.guild.id}, indent=4))

    with open(str(ctx.guild.id) + ".json", "r", encoding="utf8") as jsonfile:

        jsonfile.seek(0)

        content = json.load(jsonfile)
        content[ctx.author.voice.channel.name] = {"name": str(ctx.author.voice.channel.name),
                                                  "count": 1}
        content = json.dumps(content, indent=4, ensure_ascii=False)

    with open(str(ctx.guild.id) + ".json", "w", encoding="utf8") as jsonfile:
        jsonfile.write(content)

    await ctx.send("json file created.")



# verify if the user using the command has the admin permission
# create a .json with the server id and assign an id to this new autochannel

@bot.command(name="remove")
async def remove(ctx, id):


# remove one of the numerous autochannels defined for the server

@bot.command(name="list")
async def list(ctx):


# parse the current active autochannels and their ids from the concerned .json of the current server

async def create_new_channel(id,name):
    newname = name[:len(name)-1] + str(int(name[-1])+1)
    await discord.abc.GuildChannel.clone(name=newname, reason="autochannel")
    


# create a new channel with the same permissions in the same category with "[NAME] #[NUMBER]+1"

def rename_current_channel(id,name):
    newname = name[:len(name)-1] + str(int(name[-1])-1)
    await discord.abc.GuildChannel.edit(*,name=newname, reason="autochannel")


# rename a channel with "[NAME] #[NUMBER]-1"

def remove_channel(id):
    await discord.abc.GuildChannel.delete(*, reason="autochannel")


# remove, delete the concerned channel

def init_autochannel():
    
def remove_autochannel():

bot.run(token)
