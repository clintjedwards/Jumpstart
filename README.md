JumpStart Alarm Clock
=========

Alarm clock application that will check time and play random music file from predefined directory upon set time.

  - Uses [Threading](https://docs.python.org/2/library/threading.html) module
  - Uses [Time](https://docs.python.org/2/library/time.html)
  - Uses [Argparse](https://docs.python.org/dev/library/argparse.html) module
  - Uses/Requires [Afplay on Mac](https://developer.apple.com/library/mac/documentation/Darwin/Reference/Manpages/man1/afplay.1.html) binary


	usage: jumpstart.py [-h] [-12 TIME] [-24 TIME] [-r] [-c] [-m PATH]

	JumpStart: The Command-Line AlarmClock

	optional arguments:
  	-h, --help                show this help message and exit
  	-12 TIME, --standard TIME Use Standard Time in format: 4:23pm
  	-24 TIME, --military TIME Use Military Time in format: 15:23
  	-r, --recent              View previous alarm settings
  	-c, --clear_recent        Clear previous alarm settings
  	-m PATH, --music PATH     Define music source(Path to file or folder)


> A small, quick project that I wanted to write for personal 
> usefulness and the oppourtunity to work with threading
> Takes hours and minutes in the form of military time and 
> sets up an alarm clock to play a .mp3 file from a predefined
> folder or file.