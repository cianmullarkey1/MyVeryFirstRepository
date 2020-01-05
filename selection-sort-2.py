x = raw_input() 
a = []

while x != "end":
   a.append(int(x))
   x = raw_input()

index_lowest = input()
j = index_lowest + 1
while j < len(a):
   if a[j] < a[index_lowest]:
      index_lowest = j
   j = j + 1

print p