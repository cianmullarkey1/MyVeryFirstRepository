#!/usr/bin/env python

x = raw_input()
a = []

while x != "end":
   a.append(int(x))
   x = raw_input()

i = 0
p = 0

while i < len(a):
   if a[i] < a[p]:
      p = i 
   i = i + 1

print (p)
