list01 = [43, 15, 5, 67, 87, 9]
for r in range(len(list01) - 1):  # 0   1
    for c in range(r + 1, len(list01)):
        if list01[r] > list01[c]:
            list01[r], list01[c] = list01[c], list01[r]
print(list01)