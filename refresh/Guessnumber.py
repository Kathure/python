#Guess the number game

import random

#imported the random module because who doesn't love a bit of randomness

print "***********************"
print "   Guess the number!   "
print "***********************"

playa =raw_input("Hello player, what is your name?")
num =-1
num1 =random.randint(0,100)
while num is not num1:
   num = int(raw_input("Okay Playa, Guess a number between 0 and 100"))

   if num < num1:
      print "Sorry",playa,num,"is too LOW"

   elif num > num1:
      print "Sorry",playa,num,"is too HIGH"   

print "Good Job!DONE"


