import math
li = [int(input()) for _ in range(5)]
ans = 0
m = 0
for x in li:
  if x % 10 == 0:
      t = 0
  else:
      t = 10 - x % 10
  ans += x + t

  m = max(m,t)

print(ans-m)