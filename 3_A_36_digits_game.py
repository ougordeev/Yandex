import time
time1 = time.time()


str1 = '1111'
str2 = '9999'
from collections import deque

start = int(str1)
finish = int(str2)

def first_up(digit):
    ans = digit + 1000
    return ans

def lust_down(digit):
    ans = digit -1
    return ans

def move_left(digit):
    first = digit // 1000
    last = digit % 1000
    ans = last * 10 + first
    return ans

def move_right(digit):
    first = digit // 10
    last = digit % 10
    ans = first + last * 1000
    return ans

operations = ['fu', 'ld', 'ml', 'mr']

def bfs(digit, que, prew, j, recepy_dict, variants):
    ans = []
    i = 1
    if digit == 9911:
        pass
    for op in operations:
        if op == 'fu':
            if digit // 1000 == 9:
                continue
            else: 
                new = first_up(digit)
        elif op == 'ld':
            if digit % 10 == 1:
                continue
            else: 
                new = lust_down(digit)
        elif op == 'ml':
            new = move_left(digit)
        elif op == 'mr':
            new = move_right(digit)
        if new not in variants:
            variants.add(new)
            recepy = recepy_dict.get(prew,'')
            new_recepy = recepy + ',' + op
            recepy_dict[j+i] = new_recepy
            ans.append(new)
            que.append((new,j+i))
            i += 1
    return ans

que = deque()
j = 0
recepy_dict = {}
que.append((start,0))
find = False
variants = set()
variants.add(start)
while que:
    data = que.popleft()
    ans = bfs(data[0], que, data[1], j, recepy_dict, variants)
    for digit in ans:
        j +=1
        if digit == finish:
            find = True
            break
    if find:
        break

digit = start
print(digit)
now_recepy = recepy_dict[j].split(',')
for operation in recepy_dict[j].split(','):
    if operation == 'fu':
        new = first_up(digit)
    elif operation == 'ld':
        new = lust_down(digit)
    elif operation == 'ml':
        new = move_left(digit)
    elif operation == 'mr':
        new = move_right(digit)
    else:
        continue
    print(new)
    digit = new

print('time1 = ', time.time() - time1)
