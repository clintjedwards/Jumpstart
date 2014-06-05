JumpStart Alarm Clock
=========

A Mac OSX Alarm clock application that will check time and play random music file from predefined directory upon set time.

  - Uses [Threading](https://docs.python.org/2/library/threading.html) module
  - Uses [Time](https://docs.python.org/2/library/time.html)
  - Uses [Argparse](https://docs.python.org/dev/library/argparse.html) module
  - Uses [Pickle](https://docs.python.org/2/library/pickle.html) module
  - Uses/Requires [Afplay on Mac](https://developer.apple.com/library/mac/documentation/Darwin/Reference/Manpages/man1/afplay.1.html) binary
  - Uses/Requires [Caffeinate on Mac](https://developer.apple.com/library/mac/documentation/Darwin/Reference/Manpages/man8/caffeinate.8.html) binary


> A small, quick project that I wanted to write for personal 
> usefulness and the opportunity to work with threading.
> Takes input from user and plays a random music file from defined folder upon alarm. Tested only on Mac OS X 10.9.3+
 
<br/>




    usage: jumpstart.py [-h] [-12 TIME] [-24 TIME] [-r] [-c] [-m PATH]

    JumpStart: The Command-Line AlarmClock

    optional arguments:
      -h, --help                     show this help message and exit
      -12 <time>, --standard <time>  Use Standard Time in format: 4:23pm
      -24 <time>, --military <time>  Use Military Time in format: 15:23
      -v, --view                     View previous alarm settings
      -c, --clear_recent             Clear previous alarm settings
      -m <path>, --music <path>      Define music source(Path to file or folder)
      -s, --save                     Save alarm configuration for future use

Examples:


