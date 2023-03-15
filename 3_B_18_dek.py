
commands = ['size', 'push_back 1', 'size', 'push_back 2', 'size', 'push_front 3', 'size', 'exit']
commands.reverse()
def get_comand():
    return commands.pop()


import sys
from collections import deque
deq = deque()
lenth = 0
while True:
    com_and_value = get_comand().split()

    if com_and_value[0] == 'push_front':
        try:
            deq.appendleft(com_and_value[1])
            lenth += 1
            print('ok')
        except:
            print('error')
    elif com_and_value[0] == 'push_back':
        try:
            deq.append(com_and_value[1])
            lenth += 1
            print('ok')
        except:
            print('error')
    elif com_and_value[0] == 'size':
        print(lenth)
    elif com_and_value[0] == 'clear':
        deq.clear()
        lenth = 0
        print('ok')
    elif com_and_value[0] == 'front':
        try:
            print(deq[0])
        except:
            print('error')
    elif com_and_value[0] == 'back':
        try:
            print(deq[-1])
        except:
            print('error')
    elif com_and_value[0] == 'pop_front':
        try:
            print(deq.popleft())
            lenth -= 1
        except:
            print('error')
    elif com_and_value[0] == 'pop_back':
        try:
            print(deq.pop())
            lenth -= 1
        except:
            print('error')
    elif com_and_value[0] == 'exit':
        print('bye')
        sys.exit()

