n = int(input())
ans = 0
for i in range(7):
  if 2 ** i <= n:
    ans = 2 ** i
print(ans)