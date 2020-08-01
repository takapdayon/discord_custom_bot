import discord
import random
import numpy as np
from riotwatcher import RiotWatcher
import settings

watcher = RiotWatcher(settings.RiotAPI)

def getChannelId(message):
    try:
        if message.author.voice is not None:
            return message.author.voice.channel.id
    except UnboundLocalError as e:
        raise
    except AttributeError as e:
        raise

def getChannelMembers(client, channel_id):
    channel = client.get_channel(channel_id)
    channel_members = [i.name for i in channel.members]
    return channel_members

def groupSplit(channel_members):
    random.shuffle(channel_members)
    groups = []
    groups.append(channel_members[0::2])
    groups.append(channel_members[1::2])
    return groups

def createMessage(groups, lane_flag):

    message_stack = ""
    lanes = ["Top" , "Jg" , "Mid" , "Adc" , "Sup"]

    for gindex, group in enumerate(groups):
        message_stack += f'-チーム{gindex+1}{"-"*30}\n'
        for index, user in enumerate(group):
            if lane_flag:
                try:
                    message_stack += f'{lanes[index]}: {user}\n'
                except IndexError:
                    message_stack += f'観戦: {user}\n'
            else:
                message_stack += f'{user}\n'

    return message_stack

def addChamp(groups):
    my_region = 'jp1'
    champint = 0
    version = watcher.data_dragon.versions_for_region(my_region)
    champ_list = watcher.data_dragon.champions(version['v'], False, None)
    champions = [i for i in champ_list['data']]

    for group in groups:
        random.shuffle(champions)
        for index, user in enumerate(group):
            champ_user = f'{champions[index]} {user}'
            group[index] = champ_user
    return groups
