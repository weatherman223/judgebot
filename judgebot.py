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
            "i'm ready" in message.content or 
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

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ.get('BOT_TOKEN'))