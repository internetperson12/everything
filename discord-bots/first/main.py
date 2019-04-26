import discord
from pathlib import Path
import sys
import os
import time
import importlib
if not Path("./token.txt").is_file():
	print("No token file found. Creating\n\nPlease relaunch bot")
	open("./token.txt", 'w+')
	time.sleep(3)
	sys.exit(0)
if not Path("./prefix.txt").is_file():
	print("No prefix file found. Creating.\n\nPlease add prefix")
	open("./prefix.txt", 'w+').write("!")
	sys.exit(0)



with open("./token.txt", 'r') as token:
	if not token:
		print("NO TOKEN FOUND.")
		sys.exit(0)
	for line in token:
		token = line

with open("prefix.txt", 'r') as prefix:
	if not prefix:
		print("NO PREFIX FOUND.")
		sys.exit(0)
	for line in prefix:
		prefix = line
		
client = discord.Client()


@client.event
async def on_message(message):
	# do message stuff, implement handler
	print("Found")
	if message.author == client.user:
		return
	if message.content == "stop":
		sys.exit(0)
	if message.content.startswith(prefix):
		if message.content:
			cmd = message.content.split(" ")[0]
			cmd = cmd[1:20]
			if not Path("./cmds/{}.py".format(cmd)).is_file():
				print("Couldn't find that file.")

			else:
				handler = importlib.import_module('cmds.{}'.format(cmd))
				if not handler.permissions:
					perms_required = ['send_messages']
				else:
					perms_required = handler.permissions
				importlib.reload(handler)
				await handler.run(message.channel)
				print('\n\nFinished running file.')
@client.event
async def on_ready():
	print("logged in")
	if Path('./temp.txt').is_file():
		with open('./temp.txt', 'r') as channelsID:
			for line in channelsID:
				id_channel = line

		embed = discord.Embed()
		embed.description = "finished."
		await client.get_channel(int(id_channel)).send(embed=embed)
		os.remove("./temp.txt")

client.run(token)


async def send(msg, channel):
	await channel.send(msg)
