from discord.ext import commands
from CustomUtil import *

import discord
import random
import numpy as np
import settings
import traceback
import Constant

TOKEN = Settings.TOKEN
INITIAL_EXTENSIONS = [
    'cogs.CustomCog'
]

class Main(commands.Bot):

    def __init__(self, command_prefix):
        super().__init__(command_prefix)

        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    async def on_ready(self):
        print('-----')
        print(self.user.name)
        print(self.user.id)
        print(len(self.guilds))
        print('-----')


if __name__ == '__main__':
    bot = Main(command_prefix='!!')
    bot.run(TOKEN)
