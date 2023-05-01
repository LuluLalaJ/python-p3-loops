#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    num = 10
    while num >= 1:
        print(num)
        num -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    int_list = [int**2 for int in int_list]
    return int_list

def fizzbuzz():
    # code goes here!
    num = 1
    while num <= 100:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        num += 1


happy_new_year()
fizzbuzz()
