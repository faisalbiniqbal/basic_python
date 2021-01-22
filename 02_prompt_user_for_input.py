# -*- coding: utf-8 -*-
"""02.Prompt_User_for_Input.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ldGHJVMVVXqvOpRrewsw8zlqtnnPeiMX
"""

#We use the input() function to fetch something from user
#Anything within the parentheses will be displayed to user 

userInput = input("What's your name?") 

#UserInput is the variable where the input is stored

print("Hello",userInput)

#The comma (,) adds a space between the string and user input

# **NOTE: ALL USER DEFINED INPUTS ARE STRINGS
# If you want to take numeric values, you need to type cast them

userInputNumber1 = input("Enter first number: ")
userInputNumber2 = input("Enter second number: ")
sum = userInputNumber1 + userInputNumber2

#This sum will output "12" as both user defined numbers are treated as strings

print(sum)

#Type casting allows you to alter the types of your variables/value.
#Let's type cast the two user defined numbers

userInputNumber1 = int(userInputNumber1)
userInputNumber2 = int(userInputNumber2)
sum = userInputNumber1 + userInputNumber2

#This sum will print 3.
print(sum)

userInputNumber1 = float(userInputNumber1)
userInputNumber2 = float(userInputNumber2)
sum = userInputNumber1 + userInputNumber2

#This sum will print 3.0, as we have casted them as floating point values
print(sum)

# **NOTE: Type casting a non-numeric value into int/float will give an error.