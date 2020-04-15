import discord
from discord.ext import commands
import os
import re

bot = commands.Bot(command_prefix='!')
modulepath = "./modules"
keyfile = "./settings/dc_api_token.key"

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet(ctx):
    await ctx.send(":wave: :smiley: Hey there!")

@bot.command()
async def helloworld(ctx):
    await ctx.send("Hello World!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="SamThingsBot", description="The King of the Bots.", color=0x0000FF)

    # give info about you here
    embed.add_field(name="Author", value="SamThingElse#7553")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](https://discordapp.com/api/oauth2/authorize?client_id=522130071801298954&scope=bot)")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="SamThingsBot", description="List of commands are:", color=0x0000FF)

    embed.add_field(name="!greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="!helloworld", value='Print "Hello World!"', inline=False)
    embed.add_field(name="!cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="!info", value="Gives a little information about this bot", inline=False)
    embed.add_field(name="!help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

def apitokenreader(keyfile):
    '''
    Reads an API-Token from any file. Needs a file path as argument.

    Argument: Filepath as String.
    '''

    with open(keyfile, "r",encoding="UTF-8") as file:
        apikey = file.readline()
    return apikey

bot.run(apitokenreader(keyfile))