import subprocess
import sys
import os

class driver:
    def __init__(self, logFile):
        self.hist = [] # will hold the current history of our commands
        self.logFile = logFile

        #creates the 2 pipe processes 
        self.init()

        self.log("DRIVER STARTED")

    def init(self):
        # prepares the pipes for the logger
        self.logger = subprocess.popen(
            ['./logger', self.logFile],
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            text = True
        )

        if self.logger.poll() is not None:
            raise Exception("Logger failed to start")
        
        self.encrypt = subprocess.popen(
            ['./logger', self.logFile],
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            text = True
        )

        if self.encrypt.poll() is not None:
            raise Exception("Encryptor failed to start")
        
    def log(self, message):
        #pipes the messages to the logger
        if self.logger.stdin:
            self.logger.stdin.write(message +'\n') #this the logger activation
            self.logger.stdin.flush() # imediate send

    def incrypt(self, action):
        # this is a write to encrypt
        if self.encrypt.stdin:
            self.encrypt.stdin.write(action +'\n') #this the logger activation
            self.encrypt.stdin.flush()
                
    def outcrypt(self):        
        # this is a read from encrypt
        if self.encrypt.stdout:
            return self.encrypt.stdout.readline().strip() #this the logger activation
        return None

    def mainRun(self):
        while True:
            print("Commands")
            print("Password")
            print("Incrypt")
            print("Decrypt")
            print("History")
            print("Quit")

            action = input("Enter Command: ").strip().upper()

    
