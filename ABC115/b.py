n = int(input())
li = list(int(input()) for _ in range(n))
print(sum(li) - max(li) // 2)