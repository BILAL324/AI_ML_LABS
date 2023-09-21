# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 15:50:09 2023

@author: MINUSX
"""


import random

print ('                                      Welcome To Number Guess Game')

rand_no = random.randint(0, 100)

print(rand_no)

guesses = 100


while true:

 ges_num = int(input('Guess the number:'))

 guesses +=5
    
    
if rand_no == ges_num :
          print('well done you are right')

elif rand_no > ges_num:
           print('Guess number is Greater than the number')

elif rand_no < ges_num:
        print('Guess number is smaller than number')

else:
        print('Invalid input')
