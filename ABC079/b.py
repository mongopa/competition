N = int(input())
L = [2, 1]
if N == 1:
  print(1)
  exit()
for i in range(2, N + 1):
  L.append(L[i - 2] + L[i - 1])
print(L[-1])