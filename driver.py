import subprocess
import sys
import os

class Driver:
    def __init__(self, logFile):
        self.hist = [] # will hold the current history of our commands
        self.logFile = logFile

        #creates the 2 pipe processes 
        self.init()

        self.log("DRIVER STARTED")

    def init(self):
        # prepares the pipes for the logger
        self.logger = subprocess.Popen(
            ['python', 'logger.py', self.logFile],
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            text = True
        )

        if self.logger.poll() is not None:
            raise Exception("Logger failed to start")
        """
        self.encrypt = subprocess.Popen(
            ['./encryptor'],
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            text = True
        )

        if self.encrypt.poll() is not None:
            raise Exception("Encryptor failed to start")
        """
        self.encrypt = None # temp for logger testing
        
    def log(self, message):
        #pipes the messages to the logger
        if self.logger.stdin:
            self.logger.stdin.write(message +'\n') #this the logger activation
            self.logger.stdin.flush() # imediate send

    def outcrypt(self, action):
        # this is a write to encrypt
        if self.encryptor.stdin:
            self.encryptor.stdin.write(action +'\n') #this the logger activation
            self.encryptor.stdin.flush()
                
    def incrypt(self):        
        # this is a read from encrypt
        if self.encryptor.stdout and self.encrypt:
            return self.encryptor.stdout.readline().strip() #this the logger activation
        return "Place holder for logger testing" #None

    def mainRun(self):
        while True:
            print("\nCommands")
            print("Password")
            print("Encrypt")
            print("Decrypt")
            print("History")
            print("Quit")

            action = input("Enter Command: ").strip().upper()

            if action == "QUIT":
                self.log("ENDING PROGRAM")
                if self.logger: # cleans up the pipe before ending the program
                    self.logger.stdin.close()
                    self.logger.terminate()
                break
            elif action == "PASSWORD":
                self.password()
            elif action == "ENCRYPT":
                self.encrypt()
            elif action == "DECRYPT":
                self.decrypt()
            elif action == "HISTORY":
                self.history()
            else:
                print("Incorrect option")
                self.log(f"INVALID COMMMAND: {action}")

    def selpass(self):
        # allows for access the history for passwords
        while True:
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

    def password(self):
        self.log("PASSWORD COMMAND")

        print("Select what u want the Password to be")
        pword = self.selpass()

        if pword is None:
            return
        
        print(f"Password is {pword}")
        """
        #senting down the outpipe to the encryptor
        self.outcrypt(f"PASSKEY {pword}")

        response = self.incrypt()
        print(response)

        self.log(response)
        """

        self.log(f"PASSWORD SET")

if __name__ == "__main__": # how program runs from the command line prompt 
    
    if len(sys.argv) !=2: # checks if the right amount of arguments are giving in the commandline
        print("Wrong amount of Arguments")
        print("Should be: python driver.py logFile.log")
        sys.exit(1)
    
    logFile = sys.argv[1]
    driver = Driver(logFile)

    try:
        driver.mainRun()
    except KeyboardInterrupt:
        print("\n Program Interruption")
        driver.log("PROGRAM INTERRUPTED")
    finally:# clean up
        if driver.logger:
            driver.logger.terminate()
