s = input()
li = []
for i in range(len(s) - 2):
  li.append(abs(753 - int(s[i:i+3])))
print(min(li))