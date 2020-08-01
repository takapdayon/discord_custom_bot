from CustomUtil import *

import discord
import random
import numpy as np
import settings

TOKEN = settings.TOKEN
client = discord.Client()
ctype = ["!cus" , "!!cus" , "!!!cus"]

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    if message.content not in ctype:
        return

    try:
        channel_id = getChannelId(message)
    except UnboundLocalError as e:
        await message.channel.send("てめぇはボイスチャンネルに見当たらねぇなぁ")
    except AttributeError as e:
        await message.channel.send("AttributeError:" + str(e))

    groups = groupSplit(getChannelMembers(client, channel_id))

    lane_flag = False
    if message.content == '!!cus':
        lane_flag = True
    elif message.content == '!!!cus':
        lane_flag = True
        groups = addChamp(groups)

    send_message = createMessage(groups, lane_flag)
    await message.channel.send(send_message)

client.run(TOKEN)