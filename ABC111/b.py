n=int(input())
if n%111 == 0:
  print(n)
  exit()
print((n//111 + 1) *111)