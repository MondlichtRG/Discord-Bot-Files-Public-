# Discord-Bot-Files-Public-
# Files for Discord Bot Programming (For Public)
# This is a basic start-up you could use, may add commands to this a bit later.
# Last Updated: 29/10/21


import discord

from discord.ext import commands
prefix = '' #Use whatever prefix you want
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
  print('Bot ready to initiate')

bot.run('bot token')
