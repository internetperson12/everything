import sys
import os
from pathlib import Path
files = []
xy = os.listdir("./files/")

for file in xy:
	if file.endswith(".py"):
		files.append(str(file[0:len(file) - 3]))

if len(files) < 1:
	print("Didn't find any .py files.")
	sys.exit(0)
	
print("List of files: \n{}".format(files))

x = input("Please type name of file to run.\n\n")


if not Path("./files/{}.py".format(x)).is_file():
	print ("Couldn't find that file.")
	sys.exit(0)

else:
	print("VVV Attempting to read file. Executing code VVV \n\n")
	exec(open("./files/{}.py".format(x)).read())
	print('\n\nFinished running file.')
