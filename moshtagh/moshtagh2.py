import math
import os  #clear
os.system("cls")
def formol(number):
    f=number*math.exp(number)
    return f



number=float(input("enter the number one: "))
os.system("cls")

limit=float(input("enter the limit: "))
os .system("cls")

moshtagh2=(formol(number+limit)+formol(number-limit)-formol(number))/pow(limit,2)

print(moshtagh2)