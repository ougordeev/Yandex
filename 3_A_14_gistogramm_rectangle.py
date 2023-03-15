str2 = '8 0 0 0 0 0 0 0 1000000000'

rectangles_list = list(map(int, str2.split()))
stek = []
hi_dict = {}
ans = 0
i = -1
for rectangle in rectangles_list:
    if i == -1:
        i += 1
        continue
    exit_flag = False
    while not exit_flag:
        if stek:
            if rectangle < stek[-1][0]:
                element = stek.pop()
                len = i - element[2]
                if element[0] * len > ans:
                    ans = element[0] * len
                if (rectangle >= element[1]):
                    stek.append((rectangle, element[1], element[2]))
            else: exit_flag = True
        else: exit_flag = True
    if stek:
        if rectangle >= stek[-1][0] + 1:
            stek.append((rectangle, stek[-1][0] + 1,i))
    else:
        stek.append((rectangle, 1,i))
    i += 1

while stek:
    element = stek.pop()
    len = i - element[2]
    if element[0] * len > ans:
        ans = element[0] * len


print(ans)