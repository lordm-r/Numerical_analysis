import math
import os  #clear
os.system("cls")

def formol(number):
    f=math.exp(-1*number)
    return f


number1=float(input("enter the number one: "))
os.system("cls")
number2=float(input("enter the number two: "))
os.system("cls")

slice1=int(input("enter slice:"))+1
os.system("cls")

h=(number2-number1)/slice1

antegral=formol(number1)+formol(number2)

for i in range (1,slice1):
    if i%2==0:
        antegral=2*formol(number1+h*i)+antegral
    else:
        antegral=4*formol(number1+h*i)+antegral

antegral=antegral*h/3

print(antegral)