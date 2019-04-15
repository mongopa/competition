N, M, X = map(int, input().split())
li = map(int, input().split())
l, r = 0, 0
for i in li:
  if i < X:
    l += 1
  else:
    r += 1
print(min(l,r))