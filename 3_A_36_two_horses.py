from collections import deque

str1 = 'h1 a8'

char_digit = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

cords = str1.split()
horse_1 = (char_digit[cords[0][0]], int(cords[0][1]))
horse_2 = (char_digit[cords[1][0]], int(cords[1][1]))

di = [1, 1, -1, -1, 2, -2, 2, -2]
dj = [2, -2, 2, -2, 1, 1, -1, -1]
n = 8

horse1_set = set()
horse1_set.add(horse_1)
horse2_set = set()
horse2_set.add(horse_2)

def bfs(n, horse_set, now, que):
    for k in range(8):
        new_i = now[2] + di[k]
        new_j = now[3] + dj[k]
        if 1 <= new_i <= n and 1 <= new_j <= n:
            horse_set.add((new_i,new_j))
            que.append((now[0]+1, now[1], new_i, new_j))

que = deque()
que.append((1,1,horse_1[0],horse_1[1]))
que.append((1,2,horse_2[0],horse_2[1]))
now_steps = 0
old1_len = 0
old2_len = 0
no_ans = False
while que:
    data = que.popleft()
    if data[0] > now_steps:
        if (horse1_set & horse2_set) != set():
            break
        else:
            if len(horse1_set) == old1_len and len(horse2_set) == old2_len:
                no_ans = True
                break
            else:
                old1_len = len(horse1_set)
                old2_len = len(horse2_set)
            horse1_set = set()
            horse2_set = set()
        now_steps += 1
    if data[1] == 1:
        bfs(n, horse1_set, data, que)
    else:
        bfs(n, horse2_set, data, que)

if no_ans:
    print(-1)
else:
    print(now_steps)