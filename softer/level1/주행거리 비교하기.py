import sys


def num1(a,b):

    if a == b:
        print("same")
    elif a > b: 
        print("A")
    else:
        print("B")

a,b = map(int,input().split())

num1(a,b)
