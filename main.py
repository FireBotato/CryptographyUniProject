import base64
import itertools
#---------------------------------------------
var=""
prev=""
counter=0
def encryptceaser(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha:  
            letter_index = (alpha.find(letter) + key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

def inputmessage():

    message = input("Enter the message you want to encrypt / decrypt: ")
    return message 

def inputkey():

    key=input("Enter your key: ") 

    key=key.encode()
    key=base64.b64encode(key)
    key=key.decode()
    return key



#transforming into ascii
def transformtoascii(key):

    list=[ord(c) for c in key]
    asciiPlain=""

    #print(list)----------debug
    newlist=[]
    #fixing the problem that occurs when the key is shorter than the message so it duplicates it
    if len(list) < len(message.replace(" ","")):
        cycler=itertools.cycle(list)
        for item in cycler:
            newlist.append(item)
            if len(newlist)==len(message):
                break
        for i in newlist:
            asciiPlain+=str(i)
    
    else:

        for i in list:
            asciiPlain+=str(i)
    return asciiPlain
    #print(asciiPlain)--------debug
def encrypt(asciiPlain,message):
        for letter in message:
            global var
            global counter
            var+=encryptceaser(int(asciiPlain[counter]),letter)
            counter+=1
        counter=0
        return var
def decrypt(asciiPlain,var):
        global prev
        global counter
        for letter in var:
            prev=prev+(encryptceaser(0-int(asciiPlain[counter]),letter))
            counter+=1
        counter=0
        

message=inputmessage()
key=inputkey()
asciiPlain=transformtoascii(key)


choice=input("1.Encrypt: \n2.Decrypt:\n")
if choice=="1":
    encrypt(asciiPlain,message)
    print("The encrypted message is: ",var)
    
else:
    decrypt(asciiPlain,message)
    print("The decrypted message is: ",prev)
    

