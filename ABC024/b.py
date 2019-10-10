N, T = map(int, input().split())
ans = 0
tmp = int(input())
for i in range(N - 1):
  time = int(input())
  diff = time - tmp
  if diff < T:
    ans += diff
    tmp = time
  else:
    ans += T
    tmp = time
print(ans + T)