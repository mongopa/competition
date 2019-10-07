S = input()
N = int(input())
a = []
for i in range(5):
  for j in range(5):
    a.append(S[i]+ S[j])
print(a[N - 1])