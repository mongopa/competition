L, R = map(int, input().split())
ans = 2019
for i in range(L, min(R + 1, L + 2019 + 1)):
    for j in range(i + 1, min(R + 1, L + 2019 + 1)):
        tmp = i * j % 2019
        if tmp < ans:
            ans = tmp
print(ans)