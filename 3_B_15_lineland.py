str1 = '10'
str2 = '1 2 3 2 1 4 2 5 3 1'

n = int(str1)
lineland_list = list(map(int, str2.split()))
stek = []
moved_dict = {}

i = 0
for town in lineland_list:
    exit_flag = False
    while not exit_flag:
        if stek:
            if town < stek[-1][1]:
                moved_dict[stek.pop()[0]] = i
            else: exit_flag = True
        else: exit_flag = True  
    stek.append((i,town))
    i += 1

for i in range(n):
    print(moved_dict.get(i, -1), end= ' ')

