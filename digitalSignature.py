import hashlib

n = 170171
e = 5
d = 9677

# message to sign
message = "bob you are awesome".encode()


#step1: hash the message

sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()

h = int.from_bytes(h,'big') % n
print("hash value",h)

#sign message
sign = h**d % n

#send message with signature to bob
print(message,sign)

 
#bob verifying the signature

#step1 : calculate hash value of message

sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h = int.from_bytes(h,'big') % n
print("hash value",h)
#step2 verify the signature

verification = sign**e % n
print("Verficiation value",verification)


