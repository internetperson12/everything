import sys
import time

print("You ready to count? Let's count to 100. It'll go fast, so.. be ready\n")
time.sleep(3)
i = 0
while i < 100:
	i += 1
	sys.stdout.write("\r{}".format(str(i)))

print("\n\nOh, did I go a little too fast for you? Here, lets count to a million.\n")
time.sleep(3)
i = 0

while i < 1000000:
	i += 1
	sys.stdout.write("\r{}".format(str(i)))

print('\n\nWoah! That was a lot. Let\'s try that again sometime!')
