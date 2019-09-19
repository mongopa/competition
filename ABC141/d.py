import heapq
N, M = map(int, input().split())
li = list(map(lambda x:int(x) * (-1), input().split()))
heapq.heapify(li)
for i in range(M):
  max_price = heapq.heappop(li)*(-1)
  heapq.heappush(li, (-1) * (max_price // 2))
print(-sum(li))
