l = [int(input()) for i in range(3)]

for j in l:
  if j == min(l):
      print(3)
  elif j == max(l):
      print(1)
  else:
      print(2)