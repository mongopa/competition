s = input()
tmp = ""
for i in range(len(s)):
  if tmp == s[i]:
    print('Bad')
    exit()
  tmp = s[i]
print("Good")