"""  
    For this problem you will modify a function that creates a password
    the password needs to include features from the input list
    that contains information about the person.
    Passwords need to have 3 random special characters
    contain jumbled strings from the input
    include 2-4 numbers
    be of lenght 18-36 characters
    NOTE: 0 points if when you run the code again, the password is similar.
          Every time you run the code you should get a unique string. 
"""
import random
import string
from random import *

def passwordGenerator(personal_list): 
  characters = "personal_list" + string.ascii_letters + string.punctuation  + string.digits
  password =  "".join(choice(characters) for x in range(randint(18, 36)))
  return password



if __name__ == "__main__":
    mylist = [12,"BOB",-2,"Amy",["David","Jona","Timmothy"],"Burt"]
    print(passwordGenerator(mylist))
