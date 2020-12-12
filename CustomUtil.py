import discord
import random
import numpy as np
from riotwatcher import LolWatcher
import Settings

watcher = LolWatcher(Settings.RIOT_API)

def getChannelId(message):
    try:
        if message.author.voice is not None:
            return message.author.voice.channel.id
    except UnboundLocalError as e:
        raise
    except AttributeError as e:
        raise

def getChannelMembers(client, channel_id, exmembers=[]):
    channel = client.get_channel(channel_id)
    channel_members = []

    for member in channel.members:
        if member.nick not in exmembers and member.name not in exmembers:
            channel_members.append(member.nick if member.nick is not None else member.name)
    # channel_members = [i.nick if i.nick is not None else i.name for i in channel.members if i not in exmembers]
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
