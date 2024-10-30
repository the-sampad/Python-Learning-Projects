print('''
███████████████████████████████████████████████████████████████████████
█─▄▄▄─██▀▄─██▄─▄▄─█─▄▄▄▄██▀▄─██▄─▄▄▀███─▄▄▄─█▄─▄█▄─▄▄─█─█─█▄─▄▄─█▄─▄▄▀█
█─███▀██─▀─███─▄█▀█▄▄▄▄─██─▀─███─▄─▄███─███▀██─███─▄▄▄█─▄─██─▄█▀██─▄─▄█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▀▄▀▄▀▄▄▄▄▄▀▄▄▀▄▄▀''')
print('\n')
import string
letters = list(string.ascii_lowercase)
for i in range (10):
    letters+=letters
def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))

def enc(text,shift):
    secret_msg = ''
    
    for i in range(len(text)):
        pos = letters.index(text[i])
        secret_alpha = letters[pos+shift]
        secret_msg+=secret_alpha
    return secret_msg

def encode():
    msg = input("Normal Message : ").lower()
    shift = int(input("Shift : "))
    msg = msg.split()
    sec_msg_list = []
    for i in range(len(msg)):
        msg_part = msg[i]
        secmsg_part = enc(msg_part,shift)
        sec_msg_list.append(secmsg_part)
    secr_msg = listToString(sec_msg_list)
    print(secr_msg)

def dec(secret_msg,shift2):
    normal_msg = ''

    for i in range(len(secret_msg)):
        pos2 = letters.index(secret_msg[i])
        secret_alpha = letters[pos2-shift2]
        normal_msg+=secret_alpha
    return normal_msg

def decode():
    secret_msg = input("Secret Message : ").lower()
    shift2 = int(input("Shift : "))
    secret_msg = secret_msg.split()
    msg_list = []
    for i in range(len(secret_msg)):
        sec_msg_part = secret_msg[i]
        msg_part = dec(sec_msg_part,shift2)
        msg_list.append(msg_part)
    nor_msg = listToString(msg_list)
    print(nor_msg)
    
a = True
while a:
    operation = input('What you want to do ? Encode or Decode : ').lower()
    eval(f'{operation}()')

    cont = input("Do you like to do again ? Yes or No  :  ").lower()
    if cont=='no':
        a = False

    











