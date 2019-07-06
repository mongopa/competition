w, a, b = map(int, input().split())
diff = abs(a - b) - w
print(diff if diff > 0 else 0)