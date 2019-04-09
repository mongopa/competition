nBL = int(input())
BL= [input() for _ in range(nBL)]
nRED = int(input())
RED = [input() for _ in range(nRED)]
ans = 0
for i in set(BL):
  tmp = BL.count(i) - RED.count(i)
  if tmp > ans:
    ans = tmp

print(ans)