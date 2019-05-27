n = int(input())
l = []
while not n in l:
  l.append(n)
  if n % 2 == 0:
    n //= 2
  else:
    n = 3 * n + 1
print(len(l) + 1)