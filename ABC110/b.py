n,m,x,y= map(int, input().split())
lix = sorted(list(map(int, input().split())))
liy = sorted(list(map(int, input().split())))
if lix[-1] < liy[0] and x < liy[0] and lix[-1] < y:
  print('No War')
  exit()
print('War')

