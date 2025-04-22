import sys
import os
import random


num=int(random.randint(1,50))
guess=None
attempt=0


while guess != num:
    try:
        guess=int(input("Please enter a num"))

        attempt=attempt+1

        if guess > num:
            print("Number is high, please attempt again")

        elif guess < num:

            print("Number is low, please attempt again")
        else:

            print(f"Number Match, CONGRATS!!, you have guessed in {attempt} attempts")
    
    except ValueError:
        print("Please enter a valid integer")

