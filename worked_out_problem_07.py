# -*- coding: utf-8 -*-
"""Worked_out_Problem_07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14-vNrYadHor18JqOHwNH94vKSaHoTRac
"""

"""
~ PROBLEM 07

Assume that we have the following list
containing marks of 5 students.
marks =[10, 30, 20, 50, 40]
Find the max, min, average mark, and number of students
who got more than average mark

"""
marks =[10, 30, 20, 50, 40]

sum = 0                   #Sum of all elements in the list

marks.sort()              #Sort elements in the list

#Elements were sorted to find max and min values easily
minMarks = marks[0]       #Minimum marks
maxMarks = marks[-1]      #Maxmimum marks

count = len(marks)        #No. of elements in list

for i in marks:
  i = int(i)
  sum = sum + i

avgMarks = sum/count      #Calculate average marks

morethanAverage = 0       #Count of students who got more than average
for i in marks:
  i = int(i)
  if i>avgMarks:
    morethanAverage = morethanAverage + 1

print("The highest marks is", maxMarks, "while the lowest marks is", minMarks)
print("Average marks is", avgMarks, "and", morethanAverage, "students got more than average")