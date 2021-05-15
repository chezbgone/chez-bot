from datetime import datetime, timedelta
from time import sleep

from discord.ext import commands, tasks
from pytz import timezone

class DailyCah(commands.Cog):
    def __init__(self, bot, channelID: int):
        self.bot = bot
        self.channelID = channelID
        self.channel = None

    @commands.Cog.listener()
    async def on_ready(self):
        self.channel = self.bot.get_channel(self.channelID)
        self.send_cah.start()

    @tasks.loop(hours=24)
    async def send_cah(self):
        central_time = timezone('America/Chicago')
        year, month, date, *_ = datetime.now(tz=central_time).timetuple()
        link = f'https://www.gocomics.com/calvinandhobbes/{year}/{month}/{date}'
        await self.channel.send(link)

    @send_cah.before_loop
    async def before_send_cah(self):
        central_time = timezone('America/Chicago')
        now = datetime.now(tz=central_time)
        five_am = now.replace(hour=5, minute=0, second=0, microsecond=0)
        if five_am < now:
            five_am += timedelta(hours=24)
        sleep((five_am - now).total_seconds())
