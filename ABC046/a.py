N = int(input())
zoroli = []
n = 1
while len(zoroli) <= 50:
  s = set(str(n))
  if len(s) == 1:
    zoroli.append(n)
  n += 1
print(zoroli[N - 1])