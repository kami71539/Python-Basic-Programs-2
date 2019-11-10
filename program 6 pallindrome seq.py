# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:07:16 2019

@author: Kamran
"""

#Wap to enter 3 digit number and check for pallindrome.
num=int(input(""))
num2=num
c=100
sum=0
while num>0:
    r=num%10
    num=num//10
    sum=sum+(r*c)
    #print(sum)
    c=c//10
if sum==num2:
    print("The number is in a pallindrome sequence.")
else:
    print("The num is not in a pallindrome sequence.")