N = int(input())
if N == 1:
  print(0)
  exit()

ans = 10001
for i in range(1, N):
  mod = N % i
  tmp = abs(N // i - i)
  ans = min(ans, tmp + mod)
  
print(ans)
