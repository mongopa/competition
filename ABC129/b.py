n = int(input())
l = list(map(int, input().split()))
ansli = []
for i in range(n - 1):
  ansli.append(abs(sum(l[:i + 1]) - sum(l[i + 1:])))
print(min(ansli))