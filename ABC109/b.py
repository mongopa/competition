n = int(input())
li = [input() for _ in range(n)]
if len(set(li)) != n:
  print('No')
  exit()
for i in range(n-1):
  if li[i][-1] != li[i+1][0]:
    print('No')
    exit()
print('Yes')