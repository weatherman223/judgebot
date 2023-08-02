    # Judgebot - a discord bot that counts inspection and other easter eggs
    # Copyright (C) 2023 - Zachary Miller (weatherman223)

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.

import discord
import asyncio
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if (message.content.startswith('im ready') or 
            message.content.startswith('Im ready') or 
            message.content.startswith('Im Ready') or
            message.content.startswith('im Ready') or
            "i'm ready" in message.content or
            "I'm ready" in message.content or
            "i'm Ready" in message.content or 
            "I'm Ready" in message.content):
            # length check
            if len(message.content) in (7, 8, 9):
                # Wait for 8 seconds before sending the message.
                await asyncio.sleep(8)

                # Respond with "8 seconds."
                await message.channel.send("8 seconds")

                # Wait for 4 seconds before sending the second message.
                await asyncio.sleep(4)

                # Respond with "12 seconds."
                await message.channel.send("12 seconds")
            else:
                return
               
        if (message.content.startswith('I didnt say I was ready') or 
            message.content.startswith('i didnt say I was ready') or 
            message.content.startswith('I didnt say i was ready') or
            message.content.startswith('i didnt say i was ready') or
            "I didn't say I was ready" in message.content or 
            "i didn't say I was ready" in message.content or
            "i didn't say i was ready" in message.content or 
            "i didn't say i was ready" in message.content):
            # length check
            if len(message.content) in (22, 23, 24):
                # Respond with "PENALTY"
                await message.channel.send("PENALTY")

                return
            else:
                return


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ.get('BOT_TOKEN'))