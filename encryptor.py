import subprocess

class Encryptor:
    
    def outcrypt(self, action):
        a = action.split()
        if a[0] is "PASSKEY":
            self.setKey(a[1])
            self.incrypt(1)
        if a[0] is "ENCRYPT":
            self.encrypt()

    def incrypt(self, reponse):
        if reponse == 1:
            return "Passkey is Set"

    def setKey(self, pk):
        self.pk = pk
        self.log("[SET] Passkey Set")
        
    #def encrypt(self):
        