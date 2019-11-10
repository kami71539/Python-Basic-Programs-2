# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:10:45 2019

@author: Kamran
"""

#Wap to create a list of numbers and count the number of even and odd elements.
a=[]
b=10
count_even=0
count_odd=0
for i in range(b):
    c=int(input(""))
    a.append(c)
print(a)
for j in range(len(a)):
    if a[j]%2==0:
        count_even=count_even+1
    else:
        count_odd=count_odd+1
print(f"The number of even numbers are {count_even} and the number of odd numbers are {count_odd}")