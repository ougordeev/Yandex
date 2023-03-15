str1 = '3 2 8'
str2 = ['1', '2', '3', '1', '3', '1',  '2', '1', '2']

import heapq
from collections import deque
n,k,p = map(int,str1.split())
cars_dict = {}
play_line = []
floor = []
flor_set = set()
for i in range(p):
    car = int(str2[i])
    play_line.append(car)
    if car not in cars_dict:
        cars_dict[car] = deque()
    cars_dict[car].append(i)

count = 0
play_line.reverse()
for i in range(p):
    current_car = play_line.pop()
    while cars_dict[current_car] and i >= cars_dict[current_car][0]:
        cars_dict[current_car].popleft()
    if len(flor_set) < k:
        if current_car not in flor_set:
            flor_set.add(current_car)
            count += 1
    else:
        if current_car not in flor_set:
            exit_car = heapq.heappop(floor)
            flor_set.remove(exit_car[1])
            flor_set.add(current_car)
            count += 1
    next_request = -p -1
    if cars_dict[current_car]:
        next_request = -cars_dict[current_car].popleft()
    else:
        del cars_dict[current_car]
    heapq.heappush(floor,(next_request, current_car))
print(count)

            


