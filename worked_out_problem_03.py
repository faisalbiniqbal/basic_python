# -*- coding: utf-8 -*-
"""Worked_out_Problem_03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18axYzh5Wm4Igh2SPSVPpIgUGap3Js7UF
"""

"""
~ PROBLEM 03

Find the largest among three numbers.
Take all numbers as integers.

"""

a = input("First Number: ")
a = int(a)
b = input("First Number: ")
b = int(b)
c = input("First Number: ")
c = int(c)

if a>b:
  if a>c:
    print(a, "is the largest.")
  else:
    print(c, "is the largest.")
else:
  if b>c:
    print(b, "is the largest.")
  else:
    print(c, "is the largest.")