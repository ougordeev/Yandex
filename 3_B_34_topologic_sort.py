from threading import stack_size
from sys import setrecursionlimit

setrecursionlimit (1000000)
stack_size(134217728)

str1 = '6 6'
str2 = ['1 2', '3 2', '4 2', '2 5', '6 5', '4 6']

v,e  = map(int,str1.split())

vertex_vays = []
for i in range(v+1):
    vertex_vays.append([0,[]])

for i in range(e):
    edge = list(map(int,str2[i].split()))
    vertex_vays[edge[0]][1].append(edge[1])
    vertex_vays[edge[1]][0] += 1

vertex_dict = {}
for i in range(1,v+1):
    key = vertex_vays[i][0]
    if key not in vertex_dict:
        vertex_dict[key] = []
    vertex_dict[key].append(i)


colors = [0] * (v+1)
ans = [True]
sort = []
    
def dfs(vertex_vays, colors, sort, now):
    if not ans[0]:
        return
    colors[now] = 1
    for vay in  vertex_vays[now][1]:
        if colors[vay] == 0:
            dfs(vertex_vays, colors, sort, vay)

        else:
            if colors[vay] == 1:
                ans[0] = False
                return
    sort.append(now)
    colors[now] = 2

for key in sorted(vertex_dict.keys()):
    for vertex in vertex_dict[key]:
        if colors[vertex] == 0:
            dfs(vertex_vays, colors, sort, vertex)
sort.reverse()
if ans[0]:
    print(' '.join(list(map(str,sort))))
else:
    print('-1')