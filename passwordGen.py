import string
from random import *
import subprocess

subprocess.call(["cls"],shell=True) #Change "cls" to "clear" for linux
numInput = int(input("Enter password length: "))

chars = string.ascii_letters + string.punctuation  + string.digits
subprocess.call(["cls"],shell=True)
pword =  ''.join(choice(chars) for x in range(numInput))
print ("Password:", pword)