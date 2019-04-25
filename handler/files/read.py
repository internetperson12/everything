import sys
import time

if not Path("./files/song.txt").is_file():
	print("Couldn't find the song.txt. I'll create it for you, but, well.. I cant read a blank file.\n")
	open("./files/song.txt", 'w+')
	print('Created file! Exiting in 3 seconds')
	sys.sleep(3)
	print('Exiting!\n')
	sys.exit(0)

else:
	with open("./files/song.txt") as song:
		for line in song:
			print(line)


	print('Finished! Waiting 30 seconds before ending.')
	time.sleep(30)
