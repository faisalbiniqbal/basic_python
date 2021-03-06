# -*- coding: utf-8 -*-
"""06_lists.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qWiIg84RNwYkFKYBO3A1MId7PkNlkoj2
"""

#List is a collection which is ordered and changeable.
#Lists allow duplicate members.
# variable = [...] -> Anything within the bracket is in the list
#List items are separated by commas (,)
#Position starts from 0,1,...,n (from left)
#You can also use -1,-2,...,-n (from right) for reverse

myList = ["Apple", "Banana", "Cat", "Dog"]
# ------->   0         1        2      3
#           -4        -3       -2      -1   <--------

print(myList) #Prints the entire list
print(myList[0]) #Prints 1st element (from left) of the entire list
print(myList[3]) #Prints 4th element (from left) of the entire list
print(myList[-1]) #Prints 1st element (from right) of the entire list
print(myList[-4]) #Prints 4th element (from right) of the entire list

print(len(myList)) #Prints the size of the list

#Let's add new items to the list using listName.append("newItem")
myList.append("Elephant")
myList.append("Fish")
print(myList)
print(len(myList))

#Let's remove items from the list
#Removal using pop() -> discards the last item of the list

myList.pop()
print(myList)

#Removal using listName.remove("item") || .remove(listName[itemPosition])
myList.remove("Dog")
print(myList)
myList.remove(myList[1])
print(myList)

L1 = ["A", "B", "C", "D"]
L2 = ["E", "F", "G", "H"]

#Copying a list
L3 = L2.copy() #L3 is a new list. Contents of L2 is copied to L3.
L3.append("I")

#Clears the list. Makes the list empty.
L3.clear() #NOTE: List is NOT DELETED. IT IS JUST EMPTY. Has NO ITEMS.
print(L3)

#Deleting a list
del L3
#If you print L3 now, it will say that L3 is NOT DEFINED.
#Hence, L3 has been deleted

#Join two lists
L4 = L1 + L2
print(L4)

#Join lists using .extend(listName)
myList.extend(L4) #Takes L4 and adds its elements to the end of myList

print(myList)