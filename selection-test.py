a = []
x = raw_input()

while x != "end":
   a.append(int(x))
   x = raw_input()

i = 0
while i < len(a):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp

   i = i + 1

j = 0
while j < len(a):
   print a[j]
   j = j + 1 
