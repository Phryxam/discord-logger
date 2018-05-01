import discord
import asyncio
import datetime
import os
import json

client = discord.Client()

print("Would you like to use an account or bot token?")
print("1.Account")
print("2.Bot Token")
option=input()
if option=="1":
    print("Enter your discord e-mail here:")
    user=input()
    print("Enter your discord password here:")
    password=input()
elif option=="2":
    print("Enter the bot token:")
    token=input()
else:
    print("Something went wrong.")
print("---\n---\n---")


@client.event
async def on_ready():
    for serv in client.servers:
        print("Beginning logging of server " + serv.name)
            print("Beginning logging of channel " + chan.name)
            try:
                os.mkdir(serv.name)
            except:
                pass
            f=open(serv.name+"/"+"log-"+chan.name,"w+")
            counter=0
            #total=len(client.logs_from(chan,limit=1000000000,reverse=True))
            async for msg in client.logs_from(chan,limit=10000000000,reverse=True):
                counter+=1
                try:
                    f.write(msg.timestamp.strftime("%c")+"     "+msg.author.name + ": " + msg.clean_content+"\n")
                except:
                    f.write("Something went wrong with this message. ;w;\n")
                if len(msg.attachments)>0:
                    f.write("     ATTACHMENTS: ")
                    for att in msg.attachments:
                        f.write("        "+att['url']+"\n")
                #print("Message #" + str(counter) + "out of " + str(total))
            print("Finished logging channel " + chan.name)
    f.close()
    print("Log complete!")
		
if option=="1":
    client.run(user,password)
elif option=="2":
    client.run(token)
