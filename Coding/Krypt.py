import secrets
import string 


def ask():
    print("Hello! Welcome to Krypt! Krypt is a program to create, encrypt, and decrypt your password!")
    print
    while True:
        chc = input("Enter 1(To Create), 2(To Create), or 3(To Decrypt) your password:  ")
        try:
            int(chc)
            if chc not in (1,2,3):
                print("Please enter a number from 1 to 2, to Create, encrypt, or decrypt your password:  ")
                chc = input("Enter 1(To Create), 2(To Encrypt), or 3(To Decrypt) your password:  ")

            else:
                print(f"Amazing! Your choice is {chc}.")
                break

        except ValueError:
            print("Please enter 1, 2, or 3 to Create, Encrypt, or Decrypt your password.")
            chc = input("Enter your choice(1,2,3):  ")

def create():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    nums = string.digits
    syms = string.punctuation

    chars = lower + upper + nums + syms
    len = input("What length do you want your password to be? Type in digits. 12 is recommended:\n")
    while True:
        try:
            len = input("What length do you want your password to be? Type in digits. 12 is recommended:\n")
            len = int(len)
            if len <= 32 and len >= 8:
                print(f"Your choice is recorded as {len}.")
                break
            else:
                print("Please enter a password length more than 8 and less than 32")

        except ValueError:
            len = input("Please enter a number, which you want the length of your password to be:\n")

    charlists = [
    secrets.choice(lower),
    secrets.choice(upper),
    secrets.choice(nums),
    secrets.choice(syms)
]

    pwd = []
    for i in range(len - 4):
        pwd.append(secrets.choice(chars))
    pwd.extend(charlists)
    secrets.SystemRandom().shuffle(pwd)
    pwd = "".join(pwd)
    return pwd

