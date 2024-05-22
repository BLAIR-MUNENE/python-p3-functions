#!/usr/bin/env python3

from ast import Param


def greet_programmer():
    print("Hello, programmer!")
    return greet_programmer
  

def greet(name):
    print (f"Hello, {name}!")
    return greet
    
greet("Naureen")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    return greet_with_default

greet_with_default("Sunny")

def add(num1, num2):
    sum = num1 + num2
    print(sum)
    return sum

add(1, 2)

def halve(number):
    if isinstance(number, int):
        return number / 2
    else:
        return None
    
    
    

