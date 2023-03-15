from threading import stack_size
from sys import setrecursionlimit
setrecursionlimit (1000000)
stack_size(134217728)

# str1 = '5'
# str2 = ['0 1 0 0 0','1 0 0 0 0','0 0 0 1 1','0 0 1 0 1','0 0 1 1 0']

matrix = []
v = 0
with open('10_35', 'r') as file:
    v = int(file.readline())
    for i in range(v):
        raw = list(map(int,file.readline().split()))
        matrix.append(raw)

vertex_vays = []
for i in range(v+1):
    vertex_vays.append([])

for i in range(v):
    for j in range(i+1,v):
        if matrix[i][j] == 1:
            vertex_vays[i+1].append(j+1)
            vertex_vays[j+1].append(i+1)

colors = [0] * (v+1)
circle_detected = [False]
circle_finished = [False]
circle = []
circle_vertex = [0]

def dfs(vertex_vays, colors, circle, circle_vertex, circle_detected, circle_finished, now, prev = None):
    colors[now] = 1
    for vay in  vertex_vays[now]:
        if colors[vay] == 0:
            dfs(vertex_vays, colors, circle, circle_vertex, circle_detected, circle_finished, vay, now)
        else: 
            if prev is not None  and colors[vay] == 1 and prev != vay:
                circle_detected[0] = True
                circle_vertex[0] = vay
                circle.append(now)
                return
        if circle_detected[0]:
            break
    if circle_detected[0]:
        if circle_finished[0]:
            return
        if circle_vertex[0] == now:
            circle.append(now)
            circle_finished[0] = True
            return
        else:
            circle.append(now)
            return
    colors[now] = 2

for i in range(1,v+1):
    if colors[i] == 0:
        dfs(vertex_vays, colors, circle, circle_vertex, circle_detected, circle_finished, i)
        if circle_detected[0]:
            break

circle.reverse()
if circle_detected[0]:
    print('YES')
    print(len(circle))
    print(' '.join(list(map(str,circle))))
else:
    print('NO')