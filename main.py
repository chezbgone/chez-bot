import os

import discord
import dotenv

client = discord.Client()

if __name__ == '__main__':
    dotenv.load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    print(token)
