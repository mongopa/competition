s = input()
start = int(s[:2])
end = int(s[-2:])
if 0 < start <= 12 and 0 < end <= 12:
  print('AMBIGUOUS')
elif 0 < end <= 12:
  print('YYMM')
elif 0 < start <= 12:
  print('MMYY')
else:
  print('NA')