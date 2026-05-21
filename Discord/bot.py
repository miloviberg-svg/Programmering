import discord
from discord.ext import commands
import random
from datetime import timedelta

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=',', intents=intents)

jokes_list = [
    "I'm not just a ninja, I'm a hot ninja.",
    "What do you call an abortion center for black people\nCrime preventer!",
    "My sleep schedule and I are no longer on speaking terms\nIt died sometime around 2 a.m. scrolling",
    "I like making plans for the future\nIt gives my anxiety something new to decorate",
    "Life keeps giving me character development\nI would like to unsubscribe from this storyline.",
]

@bot.event
async def on_ready():
    print(f'Inloggad som {bot.user}')

def get_joke(joke_number):
    return jokes_list[joke_number - 1]

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send('Hello, how may I assist you today?')

@bot.command()
async def name(ctx):
    await ctx.send('My name is Kai and I am the element master of fire and I am here to assist you')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def roll(ctx):
    roll = random.randint(1,20)
    await ctx.send(f'You rolled {roll}')

@bot.command()
async def joke(ctx):
    joke_number = random.randint(1,5)
    await ctx.send(get_joke(joke_number))


@bot.command()
async def turn(ctx, text : str):
    try:
        bloody_text = ''
        for char in text:
            bloody_text = char + bloody_text
        await ctx.send(bloody_text)
    except ValueError:
        await ctx.send("hur")

@bot.remove_command("help")
@bot.command()
async def help(ctx):
    await ctx.send(',hello = a hello back \n,name = an intoduktion of myself \n,ping = I show you my very own ping \n,roll = I roll a random number for you between 1 and 20 \n,joke = I tell you a joke \n,turn = I turn whatever word you use after ",turn"')

@bot.command()
@commands.has_permissions(moderate_members=True)
async def timeout(ctx, member: discord.Member, minutes: int):
    await member.timeout(timedelta(minutes=minutes))
    await ctx.send(f"Bye Bye for now {member}")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):    #VERY IMPORTANT YOU NEED TO CAPITALIZE THE Member
    await member.kick(reason=reason)                            #kicks a person
    await ctx.send(f"Bye Bye now {member} {reason}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None): #osäker varför man behöver *, also bans a person
    await member.ban(reason=reason)
    await ctx.send(f"Bye Bye for real now {member}{reason}")

@bot.command()
async def palindrom(ctx, text : str):
    try:
        bloody_text_1 = text
        bloody_text_2 = ''
        for char in text:
            bloody_text_2 = char + bloody_text_2
        if bloody_text_2 == bloody_text_1:    
            await ctx.send("Yes!")
        else:
                await ctx.send("No")
    except ValueError:
        await ctx.send("hur")

bot.run('MTQ4MTU3MDMzODQxMTM4MDc3Nw.GDhwUW.jqpgHDQEUVb4qQCWKnfU7ijtZIw6Y-oWwymHKs')