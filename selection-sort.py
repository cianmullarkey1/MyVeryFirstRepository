import sys
import time

input = []

for line in sys.stdin.readlines():
   input.append(int(line))

startTime = time.time() 
countEls = 0 
while countEls < len(input): 
   lowestIndex = countEls
   start = countEls
   i = start
   while i < len(input):
      if (input[i] < input[lowestIndex]):
         lowestIndex = i
      i += 1


   if (lowestIndex > countEls):
      temp = input[start]
      input[start] = input[lowestIndex]
      input[lowestIndex] = temp

   countEls += 1
   # print(input)

print(input)
print ("time = " + str(time.time() - startTime))
# print (input)
