from threading import stack_size
from sys import setrecursionlimit
setrecursionlimit (1000000)
stack_size(134217728)
from collections import deque

matrix = []
v = 0
vert_start, vert_end = 0, 0

str1 = '5'
str2 = ['0 1 0 0 1','1 0 1 0 0','0 1 0 0 0','0 0 0 0 0','1 0 0 0 0']
str3 = '3 5'

v = int(str1)
for i in range(v):
    raw = list(map(int,str2[i].split()))
    matrix.append(raw)
vert_start, vert_end = map(int,str3.split())

# with open('10_35', 'r') as file:
#     v = int(file.readline())
#     for i in range(v):
#         raw = list(map(int,file.readline().split()))
#         matrix.append(raw)

vertex_vays = []
for i in range(v+1):
    vertex_vays.append([])

for i in range(v):
    for j in range(i+1,v):
        if matrix[i][j] == 1:
            vertex_vays[i+1].append(j+1)
            vertex_vays[j+1].append(i+1)

def bfs(vertex_vays, lenth_array , que, now):
    now_len = lenth_array[now]
    for vay in vertex_vays[now]:
        if lenth_array[vay] == -1:
            lenth_array[vay] = now_len + 1
            que.append(vay)
    
lenth_array = [-1] * (v + 1)
que = deque()
que.append(vert_start)
lenth_array[vert_start] = 0

while que:
    now = que.popleft()
    bfs(vertex_vays, lenth_array , que, now)
    if lenth_array[vert_end] != -1:
        break
print(lenth_array[vert_end])