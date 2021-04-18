#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: drastipatel
"""
# import libraries needed
from datetime import datetime

name             = input('What is your name? \n')
allowedUsers     = ['Seyi', 'Mike', 'Love']
allowedPasswords = ['passwordSeyi', 'passwordMike', 'passwordLove']

if(name in allowedUsers):
    password = input('Your password? \n')
    userId   = allowedUsers.index(name)

    #user should see current date and time after they login
    now = datetime.now()
    print(now.strftime('\n%H:%M:%S on %A, %B the %dth, %Y'))

    if(password == allowedPasswords[userId]):

        while True:
            print('Welcome %s' % name)
            print('These are the available options:')
            print('1. Withdraw')
            print('2. Cash Deposit')
            print('3. Complaint')

            selectedOption = int(input('Please select an option: '))

            if(selectedOption == 1):
                #get input on how much to withdraw
                amtWithdraw = input('How much would you like to withdraw? \n')
                print('Take your cash \n\n')
                pass

            elif(selectedOption == 2):
                #assuming balance is zero
                bal = 0
                #get input on how much to deposit
                amtDeposit = input('How much would you like to deposit? \n')
                curBal     = int(amtDeposit) + bal
                print('Current balance: {} \n\n'.format(curBal))
                pass

            elif(selectedOption == 3):
                #get complaint details
                complaint = input('What issue will you like to report? \n')
                print('Thank you for contacting us \n\n')
                pass

            else:
                print('Invalid option selected, please try again \n\n')

    else:
        print('Password Incorrect, please try again')

else:
    print('Name not found, please try again')
