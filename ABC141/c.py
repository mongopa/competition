N, K, Q = map(int, input().split())
points = [K - Q] * N
for i in range(Q):
  answer = int(input())
  points[answer - 1] += 1

for i in range(N):
  if points[i] > 0:
    print('Yes')
  else:
    print('No')