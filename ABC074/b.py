n = int(input())
k = int(input())
li = list(map(int, input().split()))
ans = 0
for i in range(n):
  if li[i] < k - li[i]:
    ans += li[i] * 2
  else:
    ans += (k - li[i]) * 2
print(ans)
