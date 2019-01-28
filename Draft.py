import re
import random

"""
def fibonachi(count):
    first = 0
    second = 1
    for i in range(count):
        yield second
        second = second + first
        first = second



for fib in fibonachi(10):
    print(fib)   """

"""
def subgenerator():
    yield '[subgenerator] hello'
    yield '[subgenerator] world'


def generator():
    yield '[generator] start'
    yield from subgenerator()
    yield '[generator] end'


for value in generator():
    print(value)"""


t = 'https://buyresearchpapers.db.rv.ua/'
print(t[8:-1])