str1 = '3 5'
str2 = ['2 5','5 8', '6 8', '7 8', '8 12']

import heapq
t,n = map(int, str1.split())
parkings = [i+1 for i in range(t)]
trains = []

ans = []
false_flag = False
for i in range(n):
    train = tuple(map(int,str2[i].split()))
    while trains:
        if train[0] > trains[0][0]:
            exit_train = heapq.heappop(trains)
            heapq.heappush(parkings, exit_train[1])
        else:
            break
    if parkings:
        park_num = heapq.heappop(parkings)
        heapq.heappush(trains, (train[1], park_num))
        ans.append(str(park_num))
    else:
        false_flag = True
        break
if false_flag:
    print(0,i+1)
else:
    print(' '.join(ans))


import heapq
t,n = map(int, str1.split())
parkings = [i+1 for i in range(t)]
trains = []

ans = []
false_flag = False
for i in range(n):
    train = tuple(map(int,input().split()))
    while trains:
        if train[0] > trains[0][0]:
            exit_train = heapq.heappop(trains)
            heapq.heappush(parkings, exit_train[1])
        else:
            break
    if parkings:
        park_num = heapq.heappop(parkings)
        heapq.heappush(trains, (train[1], park_num))
        ans.append(str(park_num))
    else:
        false_flag = True
        break
if false_flag:
    print(0,i+1)
else:
    print(' '.join(ans))