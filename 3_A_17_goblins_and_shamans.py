str1 = '9'
str2 = ['+ 1', '+ 2', '-', '+ 3', '+ 4', '* 5', '-', '-', '-']

from collections import deque
n = int(str1)

first_deque = deque()
first_l = 0
second_deque = deque()
second_l = 0

for i in range(n):
    request = str2[i].split()
    if request[0] == '+':
        second_deque.append(request[1])
        second_l += 1
    elif request[0] == '-':
        ans = first_deque.popleft()
        first_l -= 1
        print(ans)
    elif request[0] == '*':
        first_deque.append(request[1])
        first_l += 1
    
    if second_l > first_l:
        element = second_deque.popleft()
        second_l -= 1
        first_deque.append(element)
        first_l += 1

    if first_l > second_l+1:
        element = first_deque.pop()
        first_l -= 1
        second_deque.appendleft(element)
        second_l += 1
    
