import discord
import asyncio

client = discord.Client()

print("Bot Token:")
token=input()


@client.event
async def on_ready():
    print("hi")


@client.event
async def on_message(message):
    print(message.channel.name + "\n\t" + message.author.name + ": " +  message.clean_content)
    if len(message.attachments)>0:
        print("\t\tATTACHMENTS: ")
        for att in message.attachments:
            print("\t\t\t"+att['url'])



client.run(token)
