N = int(input())
li = [0] * (N + 2)
li[0], li[1], li[2] = 0, 0, 1
for i in range(3, N + 1):
  li[i] = (li[i - 1] + li[i - 2] + li[i - 3]) % 10007
print(li[N - 1])