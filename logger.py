import discord
import asyncio
import datetime
import os
import json

client = discord.Client()

print("Enter your discord e-mail here:")
user=input()
print("Enter your discord password here:")
password=input()
print("Enter !logServer in a server you want to log")
print("---\n---\n---")


@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	if message.content.startswith('!logServer') and message.author.name==client.user.name:
		if not os.path.exists(message.server.name):
			os.makedirs(message.server.name)
		for chan in message.server.channels:
			print("Beginning logging of channel " + chan.name)
			f=open(message.server.name+"/"+"log-"+chan.name,"w")
			async for msg in client.logs_from(chan,limit=10000000000,reverse=True):
				try:
					f.write(msg.timestamp.strftime("%c")+"     "+msg.author.name + ": " + msg.clean_content+"\n")
				except:
					f.write("Something went wrong with this message. ;w;\n")
				if len(msg.attachments)>0:
						f.write("     ATTACHMENTS: ")
						for att in msg.attachments:
							f.write("        "+att['url']+"\n")
			print("Finished logging channel " + chan.name)
			f.close()
		print("Log complete!")
		

client.run(user,password)