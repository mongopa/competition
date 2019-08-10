N = int(input())
li = list(map(int, input().split()))
tmp = li[0]
for i in range(1, N):
  if li[i] - tmp == 0:
    tmp = li[i]
  elif li[i] - tmp >= 1:
    tmp = li[i] - 1
    continue
  else:
    print('No')
    exit()
print('Yes')
