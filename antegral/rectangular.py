import math
import os  #clear
os.system("cls")
def formol(number):
    f=pow(number,2)+1
    return f



number1=float(input("enter the number one: "))
os.system("cls")
number2=float(input("enter the number two: "))
os.system("cls")

slice1=int(input("enter slice:"))+1
os.system("cls")

h=(number2-number1)/slice1
summ=0
for i in range(0,slice1):
    summ=h*( formol(number1+i*h))+summ

print("antegral=",summ)