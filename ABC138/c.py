N = int(input())
li = sorted(list(map(int, input().split())))
ans = li[0]
for i in range(1, N):
  ans = (ans + li[i]) / 2
print(ans)