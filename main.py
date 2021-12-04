import discord
from discord.ext import commands
from discord.ext.commands import cog
from discord.flags import Intents
import whybzzv2
import os

cogs = [whybzzv2]
token = os.environ["BOT_TOKEN"]
client = commands.Bot(command_prefix='?' , intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run(token)
