li = list(map(int, input().split()))
H, W = map(int, input().split())
if H in li or W in li:
  print('YES')
else:
  print('NO')