# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:41:18 2019

@author: laksh
"""

abcd = ['nintendo','Spain', 1, 2, 3]

print(abcd)
# Ex1 - Select the third element of the list and print it

print(abcd[2])
# Ex2 - Type a nested list with the follwing list elements inside list abcd mentioned above and print it

newlist= [54, 76]

abcd.append(newlist)
print(abcd)

# Ex3 - Print the 1 and the 4 position element in the following list

nestedlist = ["vagdevi", [11, 8, 4, 6], ['toronto'], abcd, "abcd"]

print(nestedlist[0])
print(nestedlist[3])

# Ex4  - add the fllowing 2 lists and create list3 and print

list1 = [10, 20, 'company', 40, 50, 100]

list2 = [100, 200, 300, 'orange', 400, 500, 1000]

list3 = list1+list2
print(list3)

# Ex 5 - print the lenght of the list3
print(len(list3))

# Ex 6 Add 320 to list 1 and print
list1.append(320)
print(list1)

# Ex 7 - Add parts of list1 & 2 by tking first 4 elements from list1 and last 2 elements from list2
first4_list1 = list1[0:4]
last2_list2 = list2[len(list2)-2:len(list2)]
print(first4_list1 + last2_list2)

# ex 8 check if 99 is in list 1
for x in list1:
    if(x==99):
        print("99 found")
        
# ex 9 check if 99 is not in list 1
for x in list1:
    if(x!=99):
       continue
    print("99 not found")
        
# ex 10 - CONCATENANTE  list 1 and ['cool', 1990]
print(list1+['cool', 1990])

# Ex 11 -  triplicate the list 1
list1*2
# ex 12 - find min & max of list2
# min(list2)  error not supported between instances of 'str' and 'int'
# max(list2)  error not supported between instances of 'str' and 'int'
min(list2)
max(list2)

# append & del
# Ex 13 append 'training' to list 1
list1.append('training')
print(list1)

# Ex 14 delete 2nd position element from list 2
list2.pop(1)
print(list2)

# Ex 15 - iterate over list1 and print all elements by adding 10 to each element
list1 = [10, 65, 20, 30, 93, 40, 50, 100]

# for x in list1:append .lis
for x in list1:
    print(x+10)
    
# Ex 16 sorting
list1.sort()
print(list1)

# sort list1 by ascending order
print(list1)

# sort list1 by reverse order
list1.sort(reverse=True)
print(list1)
