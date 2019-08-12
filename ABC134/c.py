N = int(input())
li = list(int(input()) for _ in range(N))
li_sorted = sorted(li)
max = li_sorted[-1]
premax = li_sorted[-2]
for i in range(N):
  if li[i] == max:
    print(premax)
  else:
    print(max)