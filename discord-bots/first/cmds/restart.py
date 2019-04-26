import sys
import os
permissions = []
async def run(channel):
	await channel.send("Pushing updates. I may be unresponsive for a few moments.")
	open('./temp.txt', 'w+').write(str(channel.id))
	python = sys.executable
	os.execl(python, python, * sys.argv)
	sys.exit(0)
