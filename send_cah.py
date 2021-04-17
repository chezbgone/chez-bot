import argparse
import os

import discord
from discord.ext import tasks
import dotenv

parser = argparse.ArgumentParser(description='Send a Calvin and Hobbes comic'
                                             ' to a discord server.')
parser.add_argument('channelID')

class CahClient(discord.Client):
    def __init__(self, channel_id: int, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.channel_id = channel_id
        self.send_cah.start()

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

    @tasks.loop(seconds=60)
    async def send_cah(self):
        channel = self.get_channel(self.channel_id)
        await channel.send('hello')

    @send_cah.before_loop
    async def before_send_cah(self):
        await self.wait_until_ready()


if __name__ == '__main__':
    args = parser.parse_args()
    dotenv.load_dotenv()
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    CahClient(int(args.channelID)).run(DISCORD_TOKEN)
