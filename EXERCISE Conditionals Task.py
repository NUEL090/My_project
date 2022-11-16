#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:04:18 2019

@author: NUEL
"""

'''
Question 1
Write code that asks the user to input a number between 1 and 5 inclusive.
The code will take the integer value and print out the string value. So for
example if the user inputs 2 the code will print two. Reject any input that
is not a number in that range
'''

# Input_value = int(input('Input a number between 1 to 5:>>>'))
# print('User input=',Input_value)
# if Input_value == 1:
#     print('one')
# elif Input_value == 2:
#     print('two')
# elif Input_value == 3:
#     print('three')
# elif Input_value == 4:
#     print('four')
# elif Input_value == 5:
#     print('five')
# else:
#     print('Reject input')


'''
Question 2
Repeat the previous task but this time the user will input a string and the
code will ouput the integer value. Convert the string to lowercase first.
'''
# Input__value = str(input('Input a number between 1 to 5 in word:>>>'))
# Input_value = Input__value.lower()
# print('User input=',Input_value)
# if Input_value == 'one':
#     print(1)
# elif Input_value == 'two':
#     print(2)
# elif Input_value == 'three':
#     print(3)
# elif Input_value == 'four':
#     print(4)
# elif Input_value == 'five':
#     print(5)
# else:
#     print('Reject input')



'''
Question 3
Create a variable containing an integer between 1 and 10 inclusive. Ask the
user to guess the number. If they guess too high or too low, tell them they
have not won. Tell them they win if they guess the correct number.
'''
# secret_number = 5
# user_guess = input('Guess an integer number: ')
# print('user_guess=',user_guess)
# if user_guess.isdigit():
#     user_guess = int(user_guess)
#     if user_guess == secret_number:
#         print('You win')
#     elif user_guess > secret_number and  user_guess <= 10:
#         print('Number too high, you lose')
#     elif user_guess < secret_number and  user_guess >= 1:
#         print('Number too low, you lose')
#     else:
#         print('Out of range')
# else:
#     print('Input not an integer')


'''
Question 4
Ask the user to input their name. Check the length of the name. If it is
greater than 5 characters long, write a message telling them how many characters
otherwise write a message saying the length of their name is a secret
'''
# Name = input('Please input your name: ')

# if len(Name) > 5:
#     print('Your name has',len(Name),'characters')
# else:
#     print('The length of your name is a secret')


'''
Question 5
Ask the user for two integers between 1 and 20. If they are both greater than
15 return their product. If only one is greater than 15 return their sum, if
neither are greater than 15 return zero
'''
# var_1 = int(input('Input an integer between 1 and 20: '))
# var_2 = int(input('Input another integer between 1 and 20: '))
# print('Frist input =',var_1,'\n','Second input =',var_2)
# if var_1 > 15 and var_2 > 15:
#     print('product of var_1 and var_2 =',var_1 * var_2)
# elif var_1 > 15 or var_2 > 15:
#     print('The sum of var_1 and var_2 =',var_1 + var_2)
# else:
#     print('Zero')



'''
Question 6
Ask the user for two integers, then swap the contents of the variables. So if
var_1 = 1 and var_2 = 2 initially, once the code has run var_1 should equal 2
and var_2 should equal 1.
'''
# var_3 = int(input('Input an integer called var_3: '))
# var_4 = int(input('Input another integer called var_4: '))
# print('var_3 =',var_3,'intitially, but now var_3 =',var_4)

# print('var_4 =',var_4,'intitially, but now var_4 =',var_3)


