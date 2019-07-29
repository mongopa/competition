li = ['A', 'B', 'C', 'D', 'E', 'F']
a, b = input().split()
a = li.index(a)
b = li.index(b)
if a > b:
  print('>')
elif a < b:
  print('<')
else:
  print('=')