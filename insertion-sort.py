import sys
import time

input = []

for line in sys.stdin.readlines():
   input.append(int(line))


startTime = time.time() 
countEls = 0 

# INSERTION Sort: You know the stuff behind you is sorted so find the next small one and 
# movie it back up the list?
# 1,2,3,5,4
fwdIndex = 1

while fwdIndex < len(input):
   if (input[fwdIndex] < input[fwdIndex - 1]):
      # need to move item up and *insert* somewhere above 
      # we know already that item @ [fwdIndex] < [fwdIndex -1], so they should be swapped at least

      revIndex = fwdIndex
      while revIndex > 0:
         # swap
         if (input[revIndex] < input[revIndex - 1]):
            temp = input[revIndex]
            input[revIndex] = input[revIndex - 1]
            input[revIndex - 1] = temp

         # keep going back
         revIndex = revIndex - 1

   fwdIndex = fwdIndex + 1

for entry in input:
   print (entry)
# print (input)
