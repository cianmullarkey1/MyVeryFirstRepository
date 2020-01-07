import sys
import time

input = []
for line in sys.stdin.readlines():
   input.append(int(line))

sought = 534
found = False
couldBeThere = True

start = 0
end = len(input)
 
while couldBeThere and not found:
  current = int((start + end) / 2)
  print (start),
  print (end),
  print (current),
  print ("\t:\t"),
  print (sought),
  print (input[current]),

  if sought == input[current]:
    print("Y"),
    found = True
  elif sought < input[current]:
    end = current
    print ("<")
  else:
    start = current
    print (">")

  if end - start <= 0:
    print ("N"),
    couldBeThere = False



