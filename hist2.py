import sys

input = sys.stdin.read()

i = 0
while i < len(input):
   print ("*" * int(input[i]))
   i += 1