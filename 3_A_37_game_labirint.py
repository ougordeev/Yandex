from collections import deque

str1 = '4 5'
str2 = ['0 0 0 0 1','0 1 1 0 2','0 2 1 0 0','0 0 1 0 0']

n,m = map(int,str1.split())

field = []
field.append([1]*(m+2))
for i in range(n):
    raw = [1]
    raw.extend(list(map(int,str2[i].split())))
    raw.append(1)
    field.append(raw)
field.append([1]*(m+2))


start = (1,1)

def forvard(cord,field):
    current_i = cord[0]
    current_j = cord[1]
    current_value = field[current_i-1][current_j]
    while current_value == 0:
        current_i -= 1
        current_value = field[current_i-1][current_j]
    if current_value == 1:
        return(current_i,current_j)
    else:
        return(-1,-1)

def back(cord,field):
    current_i = cord[0]
    current_j = cord[1]
    current_value = field[current_i+1][current_j]
    while current_value == 0:
        current_i += 1
        current_value = field[current_i+1][current_j]
    if current_value == 1:
        return(current_i,current_j)
    else:
        return(-1,-1)

def left(cord,field):
    current_i = cord[0]
    current_j = cord[1]
    current_value = field[current_i][current_j-1]
    while current_value == 0:
        current_j -= 1
        current_value = field[current_i][current_j-1]
    if current_value == 1:
        return(current_i,current_j)
    else:
        return(-1,-1)

def right(cord,field):
    current_i = cord[0]
    current_j = cord[1]
    current_value = field[current_i][current_j+1]
    while current_value == 0:
        current_j += 1
        current_value = field[current_i][current_j+1]
    if current_value == 1:
        return(current_i,current_j)
    else:
        return(-1,-1)

operations = ['forvard', 'back', 'left', 'right']

def bfs(cords, que, steps, variants, exit_flag, ans_steps, field):
    for op in operations:
        if op == 'forvard':
            new_cords = forvard(cords, field)
        elif op == 'back':
            new_cords = back(cords, field)
        elif op == 'left':
            new_cords = left(cords, field)
        elif op == 'right':
            new_cords = right(cords, field)
        if new_cords == (-1,-1):
            exit_flag[0] = True
            ans_steps[0] = steps+1
            return
        if new_cords not in variants:
            variants.add(new_cords)
            que.append((new_cords[0],new_cords[1],steps+1))

que = deque()
que.append((start[0],start[1],0))
exit_flag = [False]
ans_steps = [0]
variants = set()
variants.add(start)
if field[1][1] == 2:
    print(0)
else:
    while que:
        data = que.popleft()
        bfs((data[0],data[1]), que, data[2], variants, exit_flag, ans_steps, field)
        if exit_flag[0]:
            break
    print(ans_steps[0])

