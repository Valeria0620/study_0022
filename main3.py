import math
import random
n = input()
if n == '*':
    x = int(input())
    y = int(input())
    print(x * y)
elif n == '+':
    x = int(input())
    y = int(input())
    print(x + y)
elif n == '/':
    x = int(input())
    y = int(input())
    print(x / y)
elif n == '-':
    x = int(input())
    y = int(input())
    print(x - y)
elif n == '**':
    x = int(input())
    y = int(input())
    print(x ** y)
elif n == 'abs':
    x = int(input())
    print(abs(x))
elif n == 'random':
    print(random.random())
elif n == '!':
    x = int(input())
    print(math.factorial(x))
elif n == 'arccos':
    x = int(input())
    print(math.acos(x))








