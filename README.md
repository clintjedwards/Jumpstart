JumpStart Alarm Clock
=========

Alarm clock application that will check time and play random music file from predefined directory upon set time.

  - Uses [Threading](https://docs.python.org/2/library/threading.html) module
  - Uses [Time](https://docs.python.org/2/library/time.html)
  - Uses [Argparse](https://docs.python.org/dev/library/argparse.html) module
  - Uses/Requires [Afplay on Mac](https://developer.apple.com/library/mac/documentation/Darwin/Reference/Manpages/man1/afplay.1.html) binary
  
  - Command line tool: Usage: Jumpstart.py hour minutes path_to_file|folder
  - Usage example: python jumpstart.py 14 55 ~/Music/mymusic.mp3 & (Play a specific file)
  - Usage example: python jumpstart.py 14 55 ~/Music/ & (Play a file from a folder at random)
  - **ONLY ACCEPTS MILITARY TIME** for now.

> A small, quick project that I wanted to write for personal 
> usefulness and the oppourtunity to work with threading
> Takes hours and minutes in the form of military time and 
> sets up an alarm clock to play a .mp3 file from a predefined
> folder or file.