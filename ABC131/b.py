n, l = map(int, input().split())
li = [i for i in range(l, l + n)]
min = 0
if l > 0:
  min = l
elif li[-1] < 0:
  min = li[-1]
print(sum(li) - min)