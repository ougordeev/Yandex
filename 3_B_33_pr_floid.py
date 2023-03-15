from threading import stack_size
from sys import setrecursionlimit

setrecursionlimit (1000000)
stack_size(134217728)

str1 = '3 3'
str2 = ['1 2','2 3', '1 3']

v,e  = map(int,str1.split())

vertex_vays = []
for i in range(v+1):
    vertex_vays.append([])

for i in range(e):
    edge = list(map(int,str2[i].split()))
    vertex_vays[edge[0]].append(edge[1])
    vertex_vays[edge[1]].append(edge[0])



colors = [0] * (v+1)
ans = [True]
    
def dfs(vertex_vays, colors, color, now):
    if not ans[0]:
        return
    colors[now] = color
    for vay in  vertex_vays[now]:
        if colors[vay] == 0:
            dfs(vertex_vays, colors, 3-color , vay)
        else:
            if colors[vay] == color:
                ans[0] = False
                return

for i in range(1,v+1):
    if colors[i] == 0:
        dfs(vertex_vays, colors, 1, i)

if ans[0]:
    print('YES')
else:
    print('NO')