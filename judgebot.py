import discord
import asyncio
import json

# Opens the file in read-only mode and assigns the contents to the variable cfg to be accessed further down
with open('config.json', 'r') as cfg:
  # Deserialize the JSON data (essentially turning it into a Python dictionary object so we can use it in our code) 
  data = json.load(cfg) 

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith('im ready') or message.content.startswith('Im ready') or "i'm ready" in message.content or "I'm ready" in message.content:
            # Wait for 8 seconds before sending the message.
            await asyncio.sleep(8)

            # Respond with "8 seconds."
            await message.channel.send("8 seconds")

            # Wait for 4 seconds before sending the second message.
            await asyncio.sleep(4)

            # Respond with "12 seconds."
            await message.channel.send("12 seconds")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('data["token"]')