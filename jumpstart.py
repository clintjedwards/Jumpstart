"""
Alarm clock script

Checks time and plays random music from a predefined folder.
"""

import threading
#import os
import time
import sys


class jumpstart(threading.Thread):
	
	def __init__(self, hour, minute):
		threading.Thread.__init__(self)
		self.hour = hour
		self.minute = minute


	def run(self):

		while(True):

			ticks = time.localtime()
			self.current_hour = ticks[3]
			self.current_minute = ticks[4]

			self.alarm()
			time.sleep(60)
			

	def alarm(self):
		if (self.current_hour == self.hour and 
			(self.current_minute == self.minute or
			self.current_minute == self.minute-1 or 
			self.current_minute == self.minute+1)):

			print "Time to wake up!"
			sys.exit()

		else:
			print "Not Yet..."

def main():

	if ((str(sys.argv[1]).isdigit()) and 
		str(sys.argv[2]).isdigit()): 
		
		hours = int(str(sys.argv[1]))
		minutes = int(str(sys.argv[2]))

	else:
		print "\033[1;31mError: Digits only\033[0m" 
		print "Usage: jumpstart.py [hour] [minutes]"
		print "\n"
		sys.exit()

	if (1 <= hours <= 24 and 
		0 <= minutes <= 59):

		#alarmclock = jumpstart(hours,minutes)

		print "Your Alarm has been set for " + str(hours) + ":" + str(minutes)

		#alarmclock.start()
	else:
		print "\033[1;31mError: Time out of range\033[0m" 
		print "Usage: jumpstart.py [hour] [minutes]"	
		print "Usage ex: jumpstart.py 14 55"





main() 