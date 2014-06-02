#!/usr/bin/python

"""
JumpStart: The Command-Line AlarmClock

Checks time and plays random music from a predefined folder.

usage: jumpstart.py [-h] [-12 TIME] [-24 TIME] [-r] [-c] [-m PATH]

"""

import threading
import os
import time
import sys
import random
import argparse
import re
import pickle
from subprocess import call


class jumpstart(threading.Thread):

	
	def __init__(self):
		threading.Thread.__init__(self)
		self.wake_time = 0 		 #Time to Alarm
		self.music_source = None #Music Path
		self.current_hour = 0 	 #Current real-time(local) hour
		self.current_minute = 0  #Current real-time(local) minute
		self.wake_hour = 0       #Time to alarm hour
		self.wake_minute = 0     #Time to alarm minute

		if not os.path.isfile("times_storage"):

			create_list = []
			create_list.append("-12 12:00pm -m ~/Music")

			storage = open ("times_storage", 'a')
			storage.close()
	
			with open('times_storage', 'wb') as f: 
				pickle.dump(create_list, f)



	def convert_standard_time(self, wake_time):
		find_time = re.compile("^(1[0-2]|0?[1-9]):([0-5]?[0-9])")
		
		regex_result = find_time.search(wake_time)
		truncated_time = regex_result.group(0)

		fully_transformed_time = truncated_time.replace(":", "")

		find_time = re.compile("(am|pm)$")
		regex_result = find_time.search(wake_time)
		daytime = regex_result.group(0)

		if daytime == 'am':
			military_time = fully_transformed_time
			
		elif daytime == 'pm':
			military_time = str(int(fully_transformed_time) + 1200)
			
		return military_time	
	

	#Check to see if its time to alarm every 30 seconds
	def run(self, wake_time):

		while(True):

			ticks = time.localtime()
			self.current_hour = ticks[3]
			self.current_minute = ticks[4]

			self.alarm(wake_time)
			time.sleep(60)
			
	#If current hour matches alarm hour take an action
	def alarm(self, wake_time):

		self.wake_hour = int(wake_time[:2])
		self.wake_minute = int(wake_time[2:])

		
		if (self.current_hour == self.wake_hour and 
			(self.current_minute == self.wake_minute or
			self.current_minute == self.wake_minute+1 or 
			self.current_minute == self.wake_minute+2)):

			print "Time to wake up!"
				
			if self.music_source != None:	
				self.find_music(self.music_source)
					
			sys.exit()		

	def find_music(self, music_source):
		if os.path.isdir(music_source):
			self.play_random(music_source)
			
		elif os.path.isfile(music_source):
			self.play_music(music_source)
			
		else:
			print "Not a valid file or folder"	


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

	def write_storage_file(self, time, music):
		with open('times_storage', 'rb') as f: 
				times_list = pickle.load(f)

		if music != None:
			times_list.append(time + " -m " + music)
		else:
			times_list.append(time)

		with open('times_storage', 'wb') as f: 
			pickle.dump(times_list, f)

	def read_storage_file(self):
		with open('times_storage', 'rb') as f: 
			times_list = pickle.load(f)

			print ""
			for item in times_list:
				print str(times_list.index(item)+1) + ": "  + item

	def clear_storage_file(self):

		if os.path.isfile("times_storage"):
			os.remove("times_storage")
		


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
	parser.add_argument('-24','--military', help="Use Military Time in format: 15:23", required=False, action='store', nargs=1, metavar='TIME')
	parser.add_argument('-r','--recent', help="View previous alarm settings", required=False, action='store_true')
	parser.add_argument('-c','--clear_recent', help="Clear previous alarm settings", required=False, action='store_true')
	parser.add_argument('-m','--music', help="Define music source(Path to file or folder)", required=False, action='store', nargs=1, metavar='PATH')
	parser.add_argument('-s','--save', help="Save alarm configuration for future use", required=False, action='store_true')
	args = parser.parse_args()


	if len(sys.argv) == 1:
		print "The current time is " + time.strftime("%Y-%m-%d %H:%M:%S")

	#=====Standard time=====
	if (args.standard 	  != None and
	    args.military 	  == None):

		regex = re.compile("^(1[0-2]|0?[1-9]):([0-5]?[0-9])(am|pm)$")
		
		if regex.match("".join(args.standard).lower()):
			alarmclock = jumpstart()
			wake_time = alarmclock.convert_standard_time("".join(args.standard).lower())

			print "Your Alarm is set for: " + "".join(args.standard)

			if args.music:
				alarmclock.music_source = "".join(args.music)

			if args.music and args.save:
			 	alarmclock.write_storage_file("-12 " + "".join(args.standard), "".join(args.music))
			else:
			 	alarmclock.write_storage_file("-12 " + "".join(args.standard), None)

			alarmclock.run(wake_time)

	#=====Military time=====
	if (args.standard 	  == None and
	    args.military 	  != None):

		
		regex = re.compile("^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$")
		if regex.match("".join(args.military)):
			alarmclock = jumpstart()

			print "Your Alarm is set for: " + "".join(args.military)

			if args.music:
				alarmclock.music_source = "".join(args.music)

			if args.music and args.save:
			 	alarmclock.write_storage_file("-24 " + "".join(args.military), "".join(args.music))
			else:
			 	alarmclock.write_storage_file("-24 " + "".join(args.military), None)

			alarmclock.wake_time = str("".join(args.military)).replace(":", "")	
			alarmclock.run(alarmclock.wake_time)
	
	#=====Clear stored times=====	
	if (args.clear_recent == True and
	    args.recent 	  == False):

		alarmclock = jumpstart()
		alarmclock.clear_storage_file()
		

	#=====View stored times=====
	if (args.clear_recent == False and
	    args.recent 	  == True):

		alarmclock = jumpstart()
		alarmclock.read_storage_file()

	#=====Play music=====
	if (args.standard 	  == None and
	    args.military 	  == None and
	    args.clear_recent == False and
	    args.recent 	  == False and
	    args.music 		  != None):

		alarmclock = jumpstart()
		alarmclock.find_music("".join(args.music))



main() 