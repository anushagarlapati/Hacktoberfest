n = int(input())
l = list(map(int,input().split()))

l.sort(reverse = True)
m = []
i = 0
j = 0 

while i + j < 8:
  for x in range(i):
    if i + j < 8:
      j += 1
    else:
      break
  i += 1   

j = i 
i = 0 
print(l)
print(i,j)
while j < n:
  m.append(l[i])
  for x in range(i):
    if j < n:
      m.append(l[j])
      j += 1
  
  i += 1 
  
print(m)
