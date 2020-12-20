from CustomUtil import *

import discord
import random
import numpy as np
import Settings

TOKEN = Settings.TOKEN
intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)
ctype = ["!cus" , "!!cus" , "!!!cus", "!cuslist"]

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(len(client.guilds))
    print('------')

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    messages = message.content.split()
    if not messages:
        return

    cus_message = messages.pop(0)

    if cus_message not in ctype:
        return

    try:
        channel_id = getChannelId(message)
    except UnboundLocalError as e:
        await message.channel.send("てめぇはボイスチャンネルに見当たらねぇなぁ")
    except AttributeError as e:
        await message.channel.send("AttributeError:" + str(e))

    if message.content == "!cuslist":
        members = getChannelMembers(client=client, channel_id=channel_id)
        ret_message = ""
        for member in members:
            ret_message += f"{member}\n"

        await message.channel.send(ret_message)
        return

    groups = groupSplit(getChannelMembers(client=client, channel_id=channel_id, exmembers=messages.lower()))

    lane_flag = False
    if cus_message == '!!cus':
        lane_flag = True
    elif cus_message == '!!!cus':
        lane_flag = True
        groups = addChamp(groups)

    send_message = createMessage(groups, lane_flag)
    await message.channel.send(send_message)

client.run(TOKEN)