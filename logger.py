#import time
import datetime as dt 
import sys
import os

class Logger:
    def __init__(self, logFile):
        self.logFile = logFile # now i can store logFile as an instance

    def log(self, log):
        with open(self.logFile, "a", encoding="utf-8") as f: # to prevent overwriting every entry
            currDate = dt.datetime.now()
            yr, mon, day, hr, mins, _, _, _, _ = currDate.timetuple()
            f.write(f"{yr}-{mon:02d}-{day:02d} {hr:02d}:{mins:02d} [{log.strip()}]\n")
            #sys.stdout.flush() 

    #wday, month, day, clock, year = currentTime
    #print(f"{year}-{month}-{day} {clock}")

if __name__ == "__main__": # for logger testing by itself
    if len(sys.argv) !=2: # checks if the right amount of arguments are giving in the commandline
        print("Wrong amount of Arguments")
        sys.exit(1)
    
    logFile = sys.argv[1] # sets the logFile to argument 1

    logger = Logger(logFile)        
    
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
 
    
