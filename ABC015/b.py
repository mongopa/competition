import math
N = int(input())
li = []
for i in input().split():
  if int(i) > 0:
    li.append(int(i))
print(math.ceil(sum(li) / len(li)))