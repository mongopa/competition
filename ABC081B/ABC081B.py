import sys
# s = int(input())
# li = [int(_) for _ in input().split()]
# c = 0
# while True:
#   for i in range(s):
#     if li[i] % 2 == 0:
#       li[i] //= 2
#     else:
#       print(c)
#       sys.exit()
#   c += 1

import math
n = input()
a = list(map(int, input().split()))
ans = float("inf")
for i in a:
    ans = min(ans, len(bin(i)) - bin(i).rfind("1") - 1)
print(round(ans))