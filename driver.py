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

            if action == "QUIT":
                self.log("ENDING PROGRAM")
                break
            elif action == "PASSWORD":
                self.selpass()
            elif action == "INCRYPT":
                self.encrypt()
            elif action == "DECRYPT":
                self.decrypt()
            elif action == "HISTORY":
                self.history()
            else:
                print("Incorrect option")
                self.log(f"INVALID COMMMAND: {action}")

    def histAccess(self, prompt):
        # allows for access the history for passwords
        while True:
            print(f"\n{prompt}")
            print("0 for new password string \n Else use Nums for specific past strings")
            
            for i, past in enumerate(self.hist, 1): # start the emnumaration at 1
                print(f"{i} for {past}")
            print(f" From 1 to {len(self.hist)}, {len(self.hist)+1} to Cancel")
            
            try: 
                action = int(input("Choice: ")) # turns input into a int only
                
                if action == 0:
                    newpass = input("New Password (No spaces): ")
                    if newpass.isalpha():
                        return newpass
                    else:
                        print("Only Letters is allowed for Password")
            
                elif action > 0 & action <= len(self.hist):
                    return self.hist[action-1]
            
                elif action == len(self.hist)+1:
                    return None
                
                else:
                    print("Invalid Choice")

            except ValueError:
                print("Thats not an int pls try again")
        


    
