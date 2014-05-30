#!/usr/bin/python

"""
Alarm clock script

Checks time and plays random music from a predefined folder.

Usage: jumpstart.py UPDATE

"""

import threading
import os
import time
import sys
import random
import argparse
import re
from subprocess import call


class jumpstart(threading.Thread):

	
	def __init__(self, time, music_source):
		threading.Thread.__init__(self)
		self.time = time
		self.music_source = music_source

	def convert_standard_time(self, time):
		find_time = re.compile("^(1[0-2]|0?[1-9]):([0-5]?[0-9])")
		
		regex_result = find_time.search(time)
		truncated_time = regex_result.group(0)

		fully_transformed_time = truncated_time.replace(":", "")

		find_time = re.compile("(am|pm)$")
		regex_result = find_time.search(time)
		daytime = regex_result.group(0)

		if daytime == 'am':
			military_time = fully_transformed_time
			
		elif daytime == 'pm':
			military_time = int(fully_transformed_time) + 1200
			
		return military_time	
	

	#Check to see if its time to alarm every 30 seconds
	def run(self):

		while(True):

			ticks = time.localtime()
			self.current_hour = ticks[3]
			self.current_minute = ticks[4]

			self.alarm()
			time.sleep(60)
			
	#If current hour matches alarm hour take an action
	def alarm(self):
		if (self.current_hour == self.hour and 
			(self.current_minute == self.minute or
			self.current_minute == self.minute+1 or 
			self.current_minute == self.minute+2)):

			print "Time to wake up!"

			if os.path.isdir(self.music_source):
				self.play_random(self.music_source)
			
			elif os.path.isfile(self.music_source):
				self.play_music(self.music_source)
			
			else:
				print "Not a valid file or folder"
			
			sys.exit()			

	#When given a folder, search the folder for .mp3
	# and play at random
	def play_random(self, music_source):
		
		music_files = []

		#check if the directory has been ended with slash
		#for easy appending
		if music_source[-1] != '/':
			music_source = music_source + '/'

		for file in os.listdir(music_source):
			if file.endswith(".mp3"):
				music_files.append(file)

		randomized = random.randint(0, len(music_files)-1)

		randomized_file = music_source + music_files[randomized]
		self.play_music(randomized_file)

	#When file is given call local mac player and play 
	def play_music(self, music_file):
		print "Playing: " + music_file
		call(["afplay", music_file])


def main():
	
	"""
	add_argument explained:
	required=False :: Make this an optional parameter.
	action=store :: Store the value you get when this parameter is called.
	nargs=1 :: Make sure there is at least 1 other argument after this flag is set.
	metavar :: Change the help screen to better relect what should be after the flag.
	"""
	parser = argparse.ArgumentParser(description='JumpStart: The Command-Line AlarmClock')
	parser.add_argument('-12','--standard', help="Use Standard Time in format: 4:23pm", required=False, action='store', nargs=1, metavar='TIME')
	parser.add_argument('-24','--military', help="Use Military Time in format: 1523", required=False, action='store', nargs=1, metavar='TIME')
	parser.add_argument('-r','--recent', help="View previous alarm settings", required=False, action='store_true')
	parser.add_argument('-c','--clear_recent', help="Clear previous alarm settings", required=False, action='store_true')
	parser.add_argument('-m','--music', help="Define music source(Path to file or folder)", required=False, action='store', nargs=1, metavar='PATH')
	args = parser.parse_args()
	#print args
	#print len(sys.argv)
	#print args.music

	if len(sys.argv) == 1:
		print "The current time is " + time.strftime("%Y-%m-%d %H:%M:%S")

	#Standard time
	if (args.standard 	  != None and
	    args.military 	  == None and
	    args.clear_recent == False and
	    args.recent 	  == False):

		regex = re.compile("^(1[0-2]|0?[1-9]):([0-5]?[0-9])(am|pm)$")
		
		if regex.match("".join(args.standard).lower()):
			alarmclock = jumpstart("".join(args.standard).lower(), args.music)
			alarmclock.convert_standard_time(alarmclock.time)

	#Military time
	if (args.standard 	  == None and
	    args.military 	  != None and
	    args.clear_recent == False and
	    args.recent 	  == False):
		pass

		#alarmclock = jumpstart(time, music_source)
		#print args.military

"""
	#Sanity checks
	if len(sys.argv) == 1:
		print "Usage: jumpstart.py hour minutes full_path_to_folder|file &"
		print "\n"
	else:

		#Check to see that input is actually digits
		if ((str(sys.argv[1]).isdigit()) and 
			str(sys.argv[2]).isdigit()): 
		
			hours = int(str(sys.argv[1]))
			minutes = int(str(sys.argv[2]))
			music_source = str(sys.argv[3])

		else:
			print "\033[1;31mError: Digits only\033[0m" 
			print "Usage: jumpstart.py hour minutes full_path_to_folder|file &"
			print "\n"
			sys.exit()

		#Check to see that input is between the right times
		if (0 <= hours <= 23 and 
			0 <= minutes <= 59):

			#check to see if user wanted standard time
			if sys.argv[3] == '-st':
				alarmclock = jumpstart(hours,minutes,music_source)
				alarmclock.use_standard_time = True
				print alarmclock.use_standard_time
			else:
				alarmclock = jumpstart(hours,minutes,music_source)
				print alarmclock.use_standard_time

			print "Your Alarm has been set for " + str(hours).zfill(2) + ":" + str(minutes).zfill(2)

			alarmclock.start()
		

		else:
			print "\033[1;31mError: Time out of range\033[0m" 
			print "Usage: jumpstart.py hour minutes full_path_to_folder|file &"	
			print "Usage ex: jumpstart.py 14 55 ~/Music/mymusic.mp3"

"""

main() 