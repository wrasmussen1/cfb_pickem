#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 17:18:58 2024

@author: wrasmussen
"""

# import pandas as pd

# Initialize the odds as 0
odds = 0
user_bet = 0

#user_bet = int(input('Please enter how much you would like to bet. No dollar sign needed!'))
user_odds = int(input('Enter the odds of your game in +/-XXX format. \n'))

# This function will give the winnings to the user for odds above 0
def positive_odds(user_odds):
    user_bet = int(input('Please enter how much you would like to bet. No dollar sign needed! \n'))
    winnings = ((user_odds / 100) + 1)*user_bet
    winnings = round(winnings, 2)
    print('\nYour winnings will be ${} if your bet wins! \n'.format(winnings))

# This function will give the winnings to the user for odds below 0
def negative_odds(user_odds):
    user_bet = int(input('Please enter how much you would like to bet. No dollar sign needed! \n'))
    winnings = (1-(100/user_odds))*user_bet
    winnings = round(winnings, 2)
    print('\nYour winnings will be ${} if your bet wins! \n'.format(winnings))
    
# This function will determine which function to call for determining winnings
def calculate_odds(user_odds): 
    if user_odds > 0:
        positive_odds(user_odds)
    elif user_odds < 0:
        negative_odds(user_odds)
    else:
        print("error, please enter odds in a +XXX or -XXX format")
        
calculate_odds(user_odds)

# print('Your winnings will be', winnings, 'if your bet wins!')