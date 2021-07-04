import os

import discord
from discord.ext import tasks


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # channel id for my test channel
        self.channel_id = os.environ['CHANNEL_ID']
        # start the task to run in the background
        self.my_background_task.start()

    async def on_ready(self):
        print("LONG TIME NO SEE")

    @tasks.loop(seconds=10)  # task runs every 10 seconds
    async def my_background_task(self):
        channel = self.get_channel(self.channel_id)  # channel ID goes here
        await channel.send("BONG")

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in


client = MyClient()
token = os.environ['TOKEN']
client.run(token)
