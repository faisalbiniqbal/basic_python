# -*- coding: utf-8 -*-
"""Worked_out_Problem_02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12wCGWy3gA9ps9Ur15vUYeKbCVI7eLYWn
"""

"""
~ PROBLEM 02

Write a program that calculates the tax as follows:

a) No tax if you get paid less than 10,000
b) 5% tax if you get paid between 10K and 20K
c) 10% tax if you get paid more than 20K
d) NO TAX IF YOU ARE LESS THAN 18 YEARS OLD.

Take payment and age from user as inputs; then calculate tax and prints it.
Assume user always inputs correct values, as needed. 
No need for error handling.

"""

a = input("Enter age: ")
a = int(a)
if a<18:
  print("NO TAX")
else:
  p = input("Enter earning: ")
  p = float(p)
  if p<10000:
    print("NO TAX")
  elif p==10000 or p<20000:
    print(p * 0.05)
  else:
    print(p * 0.10)