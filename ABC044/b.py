words = list(input())
li = {}
for w in words:
  if w in li:
    li[w] += 1
  else:
    li[w] = 1
for i in li.values():
  if i % 2 == 1:
    print('No')
    exit()
print('Yes')