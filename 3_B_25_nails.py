str1 = '6'
str2 = '3 13 12 4 14 6'

n = int(str1)
cords = sorted(map(int,str2.split()))
ranges = [cords[i] - cords[i-1] for i in range(1,n)]
dp_list = []
dp_list.append(ranges[0])
dp_list.append(ranges[0])
for i in range(2,n):
    dp_list.append(min(dp_list[i-1], dp_list[i-2]) + ranges[i-1])
print(dp_list[-1])

