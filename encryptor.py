import subprocess
import sys
import os

class Encryptor:
    def __init__(self):
        self.pk = None

    def setKey(self, pk):
        self.pk = pk.upper()
        #print(f"Input: PASSKEY {pk}")
        #self.log("[RESULT] Passkey Set")
        return f"Output: RESULT Passkey Set"
    
    def encrypt(self, password):
        if self.pk is None:
            return "ERROR PassKey not set"
        
        pkstr = self.pk
        size = len(self.pk)
        newpw = ''
        
        for i, char in enumerate(password):
            keypos = (ord(pkstr[i % size])) - ord('A') + 1
            pwpos =  ord(char)- ord('A') + 1
            shift = keypos + pwpos
            
            if shift > 26:
                shift -= 26
            newpw+=chr(shift + ord('A') - 1)
        
        return f"RESULT {newpw}"
    
    def decrypt(self, item):
        if self.pk is None:
            return "ERROR PassKey not set"
        
        pkstr = self.pk
        size = len(self.pk)
        newpw = ''
        
        for i, char in enumerate(item):
            keypos = (ord(pkstr[i % size])) - ord('A') + 1
            itpos =  ord(char)- ord('A') + 1
            shift =  itpos - keypos
            
            if shift < 1:
                shift += 26
            newpw+=chr(shift + ord('A') - 1)
        
        return f"RESULT {newpw}"
        
    def cmd(self, action):
        a = action.upper().split()

        if a[0] == "PASSKEY":
            return self.setKey(a[1])
        elif a[0] == "ENCRYPT":
            return self.encrypt(a[1])
        elif a[0] == "DECRYPT":
            return self.decrypt(a[1])
        elif a[0] == "QUIT":
            return "QUIT"


def main():
    encryptor = Encryptor()        
    
    # Read from stdin and log each line
    while True:
        try:
            line = sys.stdin.readline()
            if not line: #if its the end of the file
                break

            #command processing
            response = encryptor.cmd(line) # takes in the action
        
            if response:
                print(response)
                sys.stdout.flush()
            
            if response == "QUIT":
                break # Ends after one command prompt

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Logger Error: {e}", file = sys.stderr)
            sys.stdout.flush()

if __name__ == "__main__": #on cmd name call of this function
    main()