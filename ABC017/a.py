ans = 0
for i in range(3):
  S, E = map(int, input().split())
  ans += S * E // 10
print(ans)