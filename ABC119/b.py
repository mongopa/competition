N = int(input())
li = [input().split() for _ in range(N)]
ans = 0
for i in range(N):
  if li[i][1] == 'JPY':
    ans += int(li[i][0])
  else:
    ans += float(li[i][0]) * 380000.0
print(ans)