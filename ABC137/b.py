K, X = map(int, input().split())
li = []
for i in range(X - K + 1, X + K):
  li.append(str(i))
print(" ".join(li))
