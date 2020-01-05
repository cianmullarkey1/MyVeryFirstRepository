import sys
from random import randint

how_many = int(sys.stdin.readline())

for n in range(0,how_many):
   print(randint(0,10000))

