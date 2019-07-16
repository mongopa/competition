n = int(input())
li = [int(input()) for _ in range(n)]
ans = 1
index = 0
if li[index] == 2:
  print(ans)
  exit()
else:
  index = li[index] - 1
  ans += 1

for i in range(1, n):
  if li[index] == 2:
    print(ans)
    exit()
  else:
    index = li[index] - 1
    ans += 1
print(-1)