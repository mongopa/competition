s = list(input() for _ in range(3))
player = ['a', 'b', 'c']
turn = 0
while True:
  if s[turn] == '':
    print(player[turn].upper())
    break
  tmp = player.index(s[turn][0])
  s[turn] = s[turn][1:]
  turn = tmp
