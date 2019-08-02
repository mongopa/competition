N = int(input())
li = list(map(int, input().split()))
ans = 0
for i in range(N - 2):
  if li[i] < li[i + 1] < li[i + 2]:
    ans += 1
  elif li[i + 2] < li[i + 1] < li[i]:
    ans += 1
print(ans)