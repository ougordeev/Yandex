import time
time1 = time.time()

from math import sqrt
from threading import stack_size
from sys import setrecursionlimit
setrecursionlimit (1000000)
stack_size(134217728)
import heapq


# str1 = '5'
# str2 =['0 0','-1 3','2 5','5 3','4 0']

# n = int(str1)
# cords = [0]*n
# for i in range(n):
#     cords[i] = tuple(map(int,str2[i].split()))

with open('12', 'r') as file:
    n = int(file.readline())
    cords = [0]*n
    for i in range(n):
        cords[i] = tuple(map(int,file.readline().split()))

ranges = []
all_ranges = set()
for i in range(n):
    raw = [0]*n
    ranges.append(raw)
for i in range(n):
    first = cords[i]
    for j in range(i+1,n):
        second = cords[j]
        lenth = (first[0] - second[0])**2 + (first[1] - second[1])**2        
        ranges[i][j] = lenth
        ranges[j][i] = lenth
        all_ranges.add(lenth)

list_all_ranges = list(all_ranges)
heapq.heapify(list_all_ranges)



def dfs_colours(vertex_vays, colors, color, now):
    colors[now] = color
    for vay in  vertex_vays[now]:
        if colors[vay] == 0:
            dfs_colours(vertex_vays, colors, 3-color , vay)
        else:
            if colors[vay] == color:
                ans[0] = False
                return
    if not ans[0]:
        return


max_l = 1

for k in range(0,(n**2 - n)// 2):
    vertex_vays = {key:[] for key in range(n)}
    min_range = heapq.heappop(list_all_ranges)
    for i in range(n):
        for j in range(i+1,n):            
            if ranges[i][j] <= min_range:
                vertex_vays[i].append(j)
                vertex_vays[j].append(i)
    
    colors = [0] * (n)
    ans = [True]

    for i in range(n):
        if colors[i] == 0:
            dfs_colours(vertex_vays, colors, 1, i)
        if not ans[0]:
            break
    if not ans[0]:
        break
    else:
        max_l = min_range


vertex_vays = {key:[] for key in range(n)}    
for i in range(n):
    first = cords[i]
    for j in range(i+1,n):
        second = cords[j]
        lenth = (first[0] - second[0])**2 + (first[1] - second[1])**2
        if lenth <= max_l:
            vertex_vays[i].append(j)
            vertex_vays[j].append(i)

colors = [0] * (n)
for i in range(n):
    if colors[i] == 0:
        dfs_colours(vertex_vays, colors, 1, i)  

min_lenth_betwen_equal = None
for i in range(n):
    for j in range(i+1,n):
        if colors[i] == colors[j]:
            equal_range = ranges[i][j]
            if (min_lenth_betwen_equal is None) or (equal_range < min_lenth_betwen_equal):
                min_lenth_betwen_equal = equal_range


print ('{:.15f}'.format(sqrt(min_lenth_betwen_equal)/2))
print (' '.join(map(str,colors)))
print('time = ', time.time() - time1)

    