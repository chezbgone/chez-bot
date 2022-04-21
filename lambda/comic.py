import asyncio
import datetime
import os

import aiohttp
from discord import Webhook, AsyncWebhookAdapter

async def send_calvin_and_hobbes():
    async with aiohttp.ClientSession() as session:
        webhook_url = os.getenv('WEBHOOK_URL')
        webhook = Webhook.from_url(webhook_url,
                adapter=AsyncWebhookAdapter(session))
        year, month, date, *_ = datetime.date.today().timetuple()
        link = f'https://www.gocomics.com/calvinandhobbes/{year}/{month}/{date}'
        await webhook.send(link, username='Calvin and Hobbes Bot')

def lambda_handler(_event, _context):
    asyncio.run(send_calvin_and_hobbes())
