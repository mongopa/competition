n = int(input())
if n<105:
  print(0)
  exit()

ans = 1
for i in range(107, n+1, 2):
  count = 0
  for j in range(1, i+1):
    if i % j == 0:
      count += 1
  if count == 8:
    ans += 1

print(ans)
