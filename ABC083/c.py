x, y = map(int, input().split())
li = []
n = x
while n < y:
  li.append(n)
  n *= 2

print(len(li))