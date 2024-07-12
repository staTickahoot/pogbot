import asyncio
import random

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# List of random dialogues
random_dialogues = ["pog", "poggers", "pog pog pog pog", "not pog", "super pog", "pogs"]

channel_id = None

def set_channel_id(new_channel_id):
    global channel_id
    channel_id = new_channel_id

# Call the function to set the channel_id
set_channel_id(channel_id)  # Initialize with None

def get_channel_id():
    global channel_id
    return channel_id

async def random_dialogue_task():
    while True:
        await asyncio.sleep(random.randint(600, 1200))  # Sleep between 3 and 12 seconds
        current_channel_id = get_channel_id()
        if current_channel_id is not None:
            channel = bot.get_channel(current_channel_id)
            if isinstance(channel, discord.TextChannel):
                await channel.send(random.choice(random_dialogues))
            else:
                print(f"Channel with ID {current_channel_id} not found.")
        else:
            print("Channel ID not set yet. Please use the !set_channel command.")

@bot.event
async def on_ready():
    if bot.user is not None:
        print(f'Logged in as {bot.user.name}')
        bot.loop.create_task(random_dialogue_task())  # Start the random dialogue task
    else:
        print("Failed to log in. Check your bot token and network connection.")

@bot.command()
async def pog(ctx):
    await ctx.send('Im very pog')

@bot.command()
async def poggers(ctx):
    await ctx.send('Im super poggers')

@bot.command()
async def set_channel(ctx, channel_id: int):
    set_channel_id(channel_id)
    await ctx.send(f"Channel ID set to {channel_id}")

bot.run('MTI2MTE0MTMyNzI1Nzc5NjcxOQ.GEQXlY.kjbGPNPWKhndKjbuPIfg35a5bnC6zo7zgxqe4I')
