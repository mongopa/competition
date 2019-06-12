li = list(map(int, input().split()))
print(sum(li) if li[0] == li[1] else max(li) * 2 - 1)