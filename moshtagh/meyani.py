import math
import os  #clear
os.system("cls")
def formol(number):
    f=math.log(number)
    return f



number=float(input("enter the number one: "))
os.system("cls")

limit=float(input("enter the limit: "))
os .system("cls")

meyani=(formol(number+limit/2)-formol(number-limit/2))/limit

print(meyani)