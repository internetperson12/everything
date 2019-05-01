# -------------------------------------------------------------------
#                   WARNING: THIS WILL COMPLETELY
#		 DELETE EVERYTHING IN SAME DIRECTORY
#		UNLESS PERMISSIONS ARE MISSING. PLEASE
#	             USE WITH EXTREME CAUTION
#	          OR.. SOMETHING ALONG THOSE LINES 
#         yeah, i was bored. no clue why anyone would use this
# -------------------------------------------------------------------

import os
import sys
import time
print("YOUR CURRENT OPERATING SYSTEM IS " + sys.platform)

if sys.platform != "win32" and sys.platform != "win64": 
	print("Sorry, you\'re using a bad OS.")
	sys.exit(0)
  # don't know if code is different for other os 



def attemptName():
	y = input("Are you sure you want to do this? It will delete EVERYTHING from the folder it is in.\n\n")
	if y.lower() != "yes" and y.lower() != "no":
		print("Invalid answer! Try \"YES\" or \"NO\"")
		attemptName()
	if y.lower() == "no":
		sys.exit(0)


def run():
	i = 0
	warns = 0
	xy = os.listdir("./")
	print("Attempting to delete everything. fetching files.")
	for file in xy:
		if file != "launch.py":
			try:
				print("Attempt: {}".format(file))
				os.remove(file)
				i += 1
			except:
				print("Error: Access denied ({})! Ignoring".format(file))
				warns += 1

			print("Next file!")
			time.sleep(0.25)

	print("\n\nFinished! Stats below")
	print("Warns: {}".format(str(warns)))
	print("Deleted: {}".format(str(i)))
	print("Overall: " + str(i) + " / " + str(i + warns))
	print("Self destruct in 5 seconds.")
	time.sleep(5)
	os.remove("launch.py")
attemptName()


run()
