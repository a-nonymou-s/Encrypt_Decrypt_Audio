# Author : MODERN CODING - ANONYMOUS

#importing modules
from cryptography.fernet import Fernet 
#key generation 
key=Fernet.generate_key()
print(key)
#creating key file
fernet = Fernet(key)
with open('key.key','wb') as filekey:
    filekey.write(key)
#reading key file
with open('key.key','rb') as filekey:
    key=filekey.read()
#reading audio file
with open('test.wav','rb') as file:
    originalaudio=file.read()
                # ENCRYPTION PHASE #
#encrypting audio file
encrypted=fernet.encrypt(originalaudio)
with open('encrypted_voice.wav','wb') as encrypted_file:
    encrypted_file.write(encrypted)
                # DECRYPTION PHASE #
fernet=Fernet(key)
#reading encrypted audio file
with open('encrypted_voice.wav','rb') as enc_file:
    encrypted=enc_file.read()
#decrypting audio
decrypted=fernet.decrypt(encrypted)
with open('decrypted_voice.wav','wb') as dec_file:
    dec_file.write(decrypted)
