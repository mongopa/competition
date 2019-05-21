n = int(input())
t, a = map(int, input().split())
li = list(map(int, input().split()))
ali = []
for i in range(n):
  ali.append(abs(a - (t - li[i] * 0.006)))
print(ali.index(min(ali)) + 1)