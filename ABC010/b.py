N = int(input())
li = list(map(int, input().split()))
ans = 0
for i in range(N):
  j = li[i]
  while j % 2 == 0 or j % 3 == 2:
    j -= 1
    ans += 1
print(ans)