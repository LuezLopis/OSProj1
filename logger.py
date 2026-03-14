#import time
import datetime as dt 
import sys
import os

class Logger:
    def log(self, log):
        currDate = dt.datetime.now()
        yr, mon, day, hr, mins, _, _, _, _ = currDate.timetuple()
        print(f"{yr}-{mon:02d}-{day:02d} {hr:02d}:{mins:02d} [{log}]")
        sys.stdout.flush() 
    #wday, month, day, clock, year = currentTime
    #print(f"{year}-{month}-{day} {clock}")

if __name__ == "__main__":
    if len(sys.argv) !=2: # checks if the right amount of arguments are giving in the commandline
        print("Wrong amount of Arguments")
        sys.exit(1)
    
    logFile = sys.argv[1] # sets the logFile to argument 1

    logger = Logger()
    
    # Read from stdin and log each line
    while True:
        try:
            line = sys.stdin.readline()
            if not line: #if its the end of the file
                break
            logger.log(line) #else logs the message

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Logger Error: {e}", file = sys.stderr)
 
    
