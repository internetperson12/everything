import time
class timer:
	def __init__(self): # Init function. Runs when you create a timer
		self.ms = 0
		self.stx = None
		self.running = False
		self.endtime = 0.00

	def start(self): # Start a timer. | Returns nothing
		self.running = True
		self.stx = round(time.time()*1000.00)


	def end(self): # End running timer. | Returns end time (Seconds)
		self.running = False
		self.endtime = round(time.time() * 1000.00) - self.stx

	def gettime(self): # Grabs time of timer. | Returns seconds of timer
		if not self.stx:
			return None
		if self.endtime:
			return self.endtime
		self.current = round(time.time() * 1000.00) - self.stx 
		self.seconds = self.current / 1000
		return self.seconds

	@staticmethod # Method is not using object so we dont need it
	def convert(time): # Takes time in seconds and converts to minutes. | Returns: Time in Minutes 

		"""Pair with <timer>.gettime() for best result. 

		EX:

		Clock = timer()
		Clock.start()
		print( Clock.convert(Clock.gettime()) ) // 0.00000000

		time.sleep(60)

		print( Clock.convert(Clock.gettime()) ) // 1.0000000"""
		if not time > 0:
			return None
		minutes = time / 60
		return minutes
