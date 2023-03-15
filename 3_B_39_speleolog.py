str1 = '3'

str2 =['','###','###','.##','','.#.','.#S','.#.','','###','...','###']

from collections import deque
n = int(str1)

cave = []

hi = 0
j = 0
level = []
spel_start = (0,0,0)

for i in range((n+1)*n):
    raw = str2[i]
    if i % (n+1) != 0:
        lewel_raw = []
        for k in range(n):
            if raw[k] == '.':
                lewel_raw.append(1)
            elif raw[k] == '#':
                lewel_raw.append(0)
            else:
                lewel_raw.append(1)
                spel_start = (j,k,hi)
        level.append(lewel_raw)
        j += 1
        if j == n:
            cave.append(level)
            level = []
            j = 0
            hi += 1

di = [-1, 1, 0, 0, 0, 0]
dj = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]


def bfs(n, ranges_dict, now, que, exit_flag, exit_range):
    current_range = ranges_dict[now]
    for k in range(6):
        new_i = now[0] + di[k]
        new_j = now[1] + dj[k]
        new_h = now[2] + dh[k]
        if 0 <= new_i < n and 0 <= new_j < n and 0 <= new_h < n:
            if cave[new_h][new_i][new_j] == 1:
                if (new_i, new_j, new_h) not in ranges_dict:
                    ranges_dict[(new_i, new_j, new_h)] = current_range + 1
                    que.append((new_i, new_j, new_h))
                if new_h == 0:
                    exit_flag[0] = True
                    exit_range[0] = current_range + 1



ranges_dict = {}
ranges_dict[spel_start] = 0
if spel_start[2] == 0:
    print(0)
else:
    que = deque()
    que.append(spel_start)
    exit_flag = [False]
    exit_range = [0]
    while que:
        cord = que.popleft()
        bfs(n, ranges_dict, cord, que, exit_flag, exit_range)
        if exit_flag[0]:
            break
    print(exit_range[0])



