a=10
b=82
if a>b:
    print("A is greater")
else:
    print("B is greater.")
#       Key  Value
fees={'Java':10000,'Python':12000,'Android':15000}
print("Java fees @ out institute is :-",end="")
print(fees.get("Java","invalid"))
print(fees.get('java','invalid'))
print(f"{a} and {b} are 2 numbers")
print(a,"and",b,"are 2 numbers.")
print("%d and %d are 2 numbers."%(a,b))


#Enter a number and find whether the given number is odd or even.
number=int(input("Enter a number "))
if number%2==0:
    print("The number is even.")
else:
    print("The nUmber is odd.")
#-----------------------------------------------
#Enter the year and find if it is leap year or not.
year=int(input("Enter the year "))
if year%4==0:
    print("The year is a leap year.")
else:
    print("THe year is not a leap year.")
#-----------------------------------------------
#ENter 3 nos and find the greatest of the three.
first_number=int(input("Enter the first number. "))
second_number=int(input("Enter the second number. "))
third_number=int(input("Enter the third number. "))
if first_number>second_number and first_number>third_number:
    print(f"{first_number} is the greatest.")
elif second_number>first_number and second_number>third_number:
    print(f"{second_number} is the greatest.")
if third_number>second_number and third_number>first_number:
    print(f"{third_number} is the greatest.")
#-----------------------------------------------
#Insert a dictionary for the week.
print("Enter a weekday:-")
weekdays={'Monday':"First","Tuesday":"Second","Wednesday":"Third","Thursday":"Fourth","Friday":"Fifth","Saturday":"Sixth","Sunday":"Seventh"}
day=input("").title()
weekday=(weekdays.get(day))
print(f"{day} is the {weekday.lower()} day of the week.")
#-----------------------------------------------
print("Enter a weekday:- ",end="")
weekdays={'Monday':"First","Tuesday":"Second","Wednesday":"Third","Thursday":"Fourth","Friday":"Fifth","Saturday":"Sixth","Sunday":"Seventh"}
day=input("").title()
weekday=(weekdays.get(day,'invalid'))
print(day,"is",(weekdays.get(day,'invalid').lower()),"day of the week.")
