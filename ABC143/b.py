N = int(input())
li = list(map(int, input().split()))
ans = 0
for i in range(N):
  print(i)
  print(li[i + 1:])
  ans += li[i] * sum(li[i + 1:])

print(ans)