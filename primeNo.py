start = int(input("Start: "))
end = int(input("End: "))
temp = []
if start in [0, 1, 2]:
    temp.append(2)

for i in range(start, end + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                if i not in temp:
                    temp.append(i)

print(temp)
