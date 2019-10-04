S = input()
li = ["A", "B", "C", "D", "E", "F"]
ans = []
for i in li:
  ans.append(str(S.count(i)))
print(" ".join(ans))