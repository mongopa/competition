N = int(input())
li = [input() for _ in range(N)]
cnt = 0
ans = ''
for i in set(li):
  if cnt < li.count(i):
    ans = i
    cnt = li.count(i)
print(ans)