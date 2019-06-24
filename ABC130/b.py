n, x = map(int, input().split())
l = list(map(int, input().split()))
ans = 1
tmp = 0
for i in range(n):
  tmp +=  l[i] 
  print(tmp)
  if tmp <= x:
    ans += 1
print(ans)