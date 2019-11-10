# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:13:20 2019

@author: Kamran
"""

#Wap to create a list of numbers and find the avg of all even numbers.
a=[]
b=10
sum=0
count=0
for i in range(b):
    c=int(input(""))
    a.append(c)
print(a)
for j in range(len(a)):
    if a[j]%2==0:
        sum=sum+a[j]
        count=count+1
avg=sum/count
print(avg)