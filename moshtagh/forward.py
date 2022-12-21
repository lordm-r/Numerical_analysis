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

forward=(-1*formol(number)+formol(number+limit))/limit

print(forward)