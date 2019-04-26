a,b = map(int, input().split())
x=0
for i in range(b-a+1):
  x += i
print(x-b)