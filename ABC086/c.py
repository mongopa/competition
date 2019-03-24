n = int(input())
flag = True
for i in range(n):
  t, x, y = map(int, input().split())
  if t < x + y or (x + y + t) % 2:
    flag = False
if flag:
  print("Yes")
else:
  print("No")
