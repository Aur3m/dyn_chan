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
    
@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel is not None and before.channel is not None: # when you was in a channel and you go in an another channel
        if after.channel.name != before.channel.name:
            try:
                with open(str(member.guild.id) + ".json", "r", encoding="utf8") as jsonfile:
                    content = json.load(jsonfile)
                    await verif_create(content, after)

                    await verif_remove(content, before)

                    with open(str(member.guild.id) + ".json", "w", encoding="utf8") as jsonfile:

                        jsonfile.write(json.dumps(content, indent=4, ensure_ascii=False))
            except:
                print("not an autochannel")

    elif before.channel is None:
        try:
            with open(str(member.guild.id) + ".json", "r", encoding="utf8") as jsonfile:
                content = json.load(jsonfile)
                await verif_create(content, after)

            with open(str(member.guild.id) + ".json", "w", encoding="utf8") as jsonfile:
                jsonfile.write(json.dumps(content, indent=4, ensure_ascii=False))

        except:
            print("not an autochannel")

    elif after.channel is None:
        try:
            with open(str(member.guild.id) + ".json", "r", encoding="utf8") as jsonfile:
                content = json.load(jsonfile)
                await verif_remove(content, before)

            with open(str(member.guild.id) + ".json", "w", encoding="utf8") as jsonfile:
                jsonfile.write(json.dumps(content, indent=4, ensure_ascii=False))

        except:
            print("not an autochannel")

@bot.command(name="help")
async def help(ctx):
    embed=discord.Embed(title="Current Prefix ", description="**c!**")
    embed.set_author(name="Usage & Commands")
    embed.set_thumbnail(url="https://i.imgur.com/GKadtia.png")
    embed.add_field(name="create", value="[Admin Only] You need to go in a voice channel and process with this command to make this channel automatic, the same permissions and category of the inital channel will be used. The channel doesn't need to contain any number or # as they will be added during the process", inline=False)
    embed.add_field(name="remove_autochannel [name]", value="[Admin Only] Remove an autochannel using its specific name, all channels will be deleted once all players left", inline=False)
    embed.add_field(name="list", value="List all the current autochannels of the server and their ID(s)", inline=False)
    await ctx.send(embed=embed)


# print "help" text


@bot.command(name="create")
async def create(ctx):
    is_clear = False
    #print(type(ctx.author.voice.channel.name))
    #print(ctx.author.roles)
    if ctx.author.voice.channel is None or ctx.message.author.guild_permissions.administrator == False:
        return await ctx.send("you must be in a voice channel and an admin to use this command.")

    try:
        with open(str(ctx.guild.id) + ".json", "r", encoding="utf8") as jsonfile:
            if jsonfile.read() == "":
                is_clear = True
    except:
        with open(str(ctx.guild.id) + ".json", "w", encoding="utf8") as jsonfile:
            jsonfile.write(json.dumps({"guild_id": ctx.guild.id}, indent=4))

    with open(str(ctx.guild.id) + ".json", "r", encoding="utf8") as jsonfile:

        jsonfile.seek(0)

        content = json.load(jsonfile)
        content[ctx.author.voice.channel.name] = {"name": ctx.author.voice.channel.name,
                                                  "category": ctx.author.voice.channel.category.id,
                                                  "count": 1}
        content = json.dumps(content, indent=4, ensure_ascii=False)

    with open(str(ctx.guild.id) + ".json", "w", encoding="utf8") as jsonfile:
        jsonfile.write(content)

    await ctx.author.voice.channel.edit(name=ctx.author.voice.channel.name + " #1")
    await ctx.send("json file created.")


# verify if the user using the command has the admin permission
# create a .json with the server id and assign an id to this new autochannel

@bot.command(name="list")
async def list(ctx):
    with open(str(ctx.guild.id) + ".json", "r", encoding="utf8") as jsonfile:
        content = json.load(jsonfile)
        embed = discord.Embed(title="Autochanels ", description="list of all the autochannel of the server.")

        for i in content.keys():
            try:

                channel_list = ctx.guild.get_channel(content[i]["category"]).voice_channels
                print(channel_list)
                value = ""
                for j in channel_list:
                    if j.name[:len(j.name)-3] == i:
                        value += j.name +" / " + str(j.id) + "\n"
                embed.add_field(name=i, value=value, inline=False)
            except:
                print("not this")
        await ctx.send(embed=embed)


# parse the current active autochannels and their ids from the concerned .json of the current server

async def create_new_channel(channel):
    newname = channel.name[:len(channel.name)-1] + str(int(channel.name[-1])+1)
    await channel.clone(name=newname, reason="autochannel")

# create a new channel with the same permissions in the same category with "[NAME] #[NUMBER]+1"


async def rename_current_channel(channel):
    newname = channel.name[:channel.name.find("#")+1] + str(int(channel.name[channel.name.find("#")+1:])-1)
    await channel.edit(name=newname, reason="autochannel")

# rename a channel with "[NAME] #[NUMBER]-1"


async def remove_channel(channel):
# remove, delete the concerned channel
    await channel.delete(reason="autochannel_del")
    for i in channel.category.channels:
        print("i " + i.name[:i.name.find("#")])
        if i.name[:i.name.find("#")] == channel.name[:channel.name.find("#")]:
            await rename_current_channel(i)


async def verif_create(content, after):
    if after.channel.name[:after.channel.name.find("#")-1] in content.keys():

        content[after.channel.name[:after.channel.name.find("#")-1]]["count"] += 1
        await create_new_channel(after.channel)


async def verif_remove(content, before):
    print("verif_remove "+ before.channel.name[:before.channel.name.find("#")-1])
    if before.channel.name[:before.channel.name.find("#")-1] in content.keys():
        if content[before.channel.name[:before.channel.name.find("#")-1]]["count"] - 1 == 0:
            pass
        else:
            content[before.channel.name[:before.channel.name.find("#")-1]]["count"] -= 1
            await remove_channel(before.channel)


bot.run(token)
