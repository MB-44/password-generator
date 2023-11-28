import random
import string

def generatePassword(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

if __name__=="__main__":
    pw = generatePassword(16)
    print(pw)