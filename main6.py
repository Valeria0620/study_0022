import math
import random

print("Введите действие: +, -, /, -, **, abs, random, !, factorial, arccos")


def su(arg1, arg2):
    print(int(arg1 + arg2))


def dif(arg1, arg2):
    print(int(arg1 - arg2))


def mul(arg1, arg2):
    print(int(arg1 * arg2))


def div(arg1, arg2):
    print(int(arg1 / arg2))


def po(arg1, arg2):
    print(int(arg1 ** arg2))


n = input("Ваше действие: ")

if n == '*':
    mul(int(input("Число1: ")), int(input("Число2: ")))
elif n == '+':
    su(int(input("Число1: ")), int(input("Число2: ")))
elif n == '/':
    div(int(input("Число1: ")), int(input("Число2: ")))
elif n == '-':
    dif(int(input("Число1: ")), int(input("Число2: ")))
elif n == '**':
    po(int(input("Число1: ")), int(input("Число2: ")))
elif n == 'abs':
    print(abs(int(input("Число: "))))
elif n == 'random':
    print(random.random())
elif n == '!':
    print(math.factorial(int(input("Число: "))))
elif n == 'arccos':
    print(math.acos(int(input("Число: "))))
