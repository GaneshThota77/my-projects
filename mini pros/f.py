from cryptography.fernet import Fernet

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
write_key()"""

def load_key():
    file=open("key.key", "rb")
    key = file.read()
    file.close
    return key

master_pwd = input("what is the master password?:")
key= load_key() + master_pwd.encode()
fer = Fernet(key)

#pwd = input("What is the master password?")

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data=(line.rstrip())
            user,passw =data.split("|")
            print("user:",user, " |password:",str(fer.encrypt(passw.encode())))

def add():
    name= input('Account Name:')
    pwd = input("password:")

    with open('password.txt','a') as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode())).decode() +"\n")


while True:
    mode =input("Would you like to add a password or view existing once(view/add) press q to quit?:").lower()
    if mode =="q":
        break

    if mode =="view":
        view()
    elif mode=="add":
        add()
    else:
        print("invalid mode.")
        continue