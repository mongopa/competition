A, B, X = map(int, input().split())
if A % X == 0:
  print(B // X - A // X + 1)
else:
  print(B // X - A // X)