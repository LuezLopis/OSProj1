#import time
import datetime as dt 

class logger:
    def log(self, log):
        currDate = dt.datetime.now()
        yr, mon, day, hr, mins, _, _, _, _ = currDate.timetuple()
        print(f"{yr}-{mon}-{day} {hr}:{mins} [{log}]")
    
    #wday, month, day, clock, year = currentTime
    #print(f"{year}-{month}-{day} {clock}")
    
