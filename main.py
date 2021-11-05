import discord
from discord.ext import commands
from discord.ext.commands import cog
from discord.flags import Intents
import whybzzv2

cogs = [whybzzv2]

client = commands.Bot(command_prefix='?' , intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run("OTA2MTgzODg3OTM4NTI3Mjk0.YYU7gg.2iIx7_Ux9NuK-zaBJbwLyyvgMzg")

# https://www.youtube.com/watch?v=iv7lcUkFVSc #