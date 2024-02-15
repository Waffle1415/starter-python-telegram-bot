# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os
import discord
from keep import keep_alive
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if client.user in message.mentions:
    #メンションをしたユーザーに1時間後にリマインドする
    await message.channel.send(f"{message.author.mention} 10分後にリマインドします")
    #1時間後にリマインドする
    await asyncio.sleep(600)
    await message.channel.send(f"{message.author.mention} 時間です")

  if message.content == "!help":
    await message.channel.send("なんでしょう？")


try:
  token = os.getenv("TOKEN") or ""
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  keep_alive()
  try:
    client.run(os.environ['TOKEN'])
  except:
    os.system("kill")

except discord.HTTPException as e:
  if e.status == 429:
    print(
        "The Discord servers denied the connection for making too many requests"
    )
    print(
        "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
    )
  else:
    raise e
