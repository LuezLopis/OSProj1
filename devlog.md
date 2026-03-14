# 3/5 4:01 pm
- Created and connected the project git repository to GitHub, and started to understand the project 
# 3/6 10.26 am
- decided to work on the project using Python as it's the language that I'm least comfortable with, and I want to practice.
- I will lay the groundwork for the logger, with just a function that takes in a response and prints it into the format.
- Choose to use the datetime function to obtain the date and time for the logger's output.
# 6:41
- Starting to work on the encryptor, thinking just to do a basic if-else/case function to deal with the encryption commands
# 3/8 readded
- researching how to use Python subprocess
- continuing on the encryptor
# 3/13 readded
- due to an unexpected crash, progress was lost, decided to work on it again tmw
# 3/14 (definitely gonna be late TT)
- think that all the beginning stuff, like starting up the logger, will be a single initial function in the driver program
- Maybe a good idea to merge all pipe interactions, like all logger log work in one def and all encrypt reads and writes in another.
- add an extra parameter to the encrypt communication to allow for type, in, or out
- can't combine the two functions due to the need for a return function for the out, but not really for the in w/o causing other issues.
- add upper case for the case insensitivity, cuz big letters are cooler
- saving all progress now to prevent past issue of progress loss
- Gonna enumerate the hist for easy numbering, very clean and compact, 
- can't really use an if statement to check if the input is a number
- solution: try statement with exception catching
- added isaphla for letters only for the password
- now continuing on the password action function
- finished driver side of password function, has pipes to logger and read and write from encryptor
- Pausing on the driver side of the program to work on the logger, I forgot to set up the pipelines for the driver to communicate with the logger
- The log file pipe reading and file writing is very similar to how things worked in Unix and C++ piping and file writing, tho the flexible type casting is different
- ok for now, the log is hooked up to output the logs to the terminal, not a file for now
- ran it to an issue testing, it won't run a test run
- solution: popen is incorrect, it needs to be  Popen
- as so completely forgot to add the command line read, the __main__ and argv read .... bruh
- driver program runs, but it's hard to really tell if the logger is working properly, so imma just gonna add the filed output to logfile.log
- small issue with the file.write as it is not appending the txt file
- solution: used the wrong naming convenction for the log function, file as a parameter, then named the open function as file as well as opening "LogFile" which doesn't exist
Thus, I swapped logFile with File and named the funct as f. Also dont need sys.flush() as I'm going to a file
- logger has been completed so i will resume working on driver commands 
- finishing the encryptor again
