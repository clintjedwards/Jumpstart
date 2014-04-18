"""
Alarm clock script

Checks time and plays random music from a predefined folder.
"""

import threading
import os
import time
import sys
import random
from subprocess import call


class jumpstart(threading.Thread):
	
	def __init__(self, hour, minute, folder):
		threading.Thread.__init__(self)
		self.hour = hour
		self.minute = minute
		self.folder = folder


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
			#play music file here
			sys.exit()

		else:
			print "Not Yet..."

	
	def play_random(self, folder):
		
		music_files = []

		for file in os.listdir(folder):
			if file.endswith(".mp3"):
				music_files.append(file)

		randomized = random.randint(0, len(music_files)-1)

		randomized_file = folder + music_files[randomized]
		print randomized
		print randomized_file
		self.play_music(randomized_file)


	def play_music(self, music_file):
		call(["afplay", music_file])


def main():

	#If file choose file
	#If folder play random


	if ((str(sys.argv[1]).isdigit()) and 
		str(sys.argv[2]).isdigit()): 
		
		hours = int(str(sys.argv[1]))
		minutes = int(str(sys.argv[2]))
		music_source = str(sys.argv[3])

	else:
		print "\033[1;31mError: Digits only\033[0m" 
		print "Usage: jumpstart.py hour minutes folder|file"
		print "\n"
		sys.exit()

	if (1 <= hours <= 24 and 
		0 <= minutes <= 59):

		alarmclock = jumpstart(hours,minutes,music_source)

		print "Your Alarm has been set for " + str(hours) + ":" + str(minutes)
		#alarmclock.play_music(folder)
		alarmclock.play_random(music_source)

		#alarmclock.start()
	else:
		print "\033[1;31mError: Time out of range\033[0m" 
		print "Usage: jumpstart.py [hour] [minutes]"	
		print "Usage ex: jumpstart.py 14 55"



main() 