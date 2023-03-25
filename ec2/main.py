import os

from discord.ext import commands
from dotenv import load_dotenv
from daily_cah import DailyCah

if __name__ == '__main__':
    load_dotenv()
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    CAH_CHANNEL_ID = int(os.getenv('CAH_CHANNEL'))

    bot = commands.Bot(command_prefix='<@832757137158701067> ')

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')

    bot.add_cog(DailyCah(bot, CAH_CHANNEL_ID))
    bot.run(DISCORD_TOKEN)
