N = int(input())
li = sorted(list(map(int, input().split())))
dif = li[N // 2] - li[N // 2 - 1]
if dif > 0:
  print(dif)
else:
  print(0)
