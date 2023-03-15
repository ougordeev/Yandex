
commands = ['push 3', 'push 14', 'size', 'clear', 'push 1', 'front', 'push 2', 'front', 'pop', 'size', 'pop', 'size', 'exit']
commands.reverse()
def get_comand():
    return commands.pop()


import sys
from collections import deque
deq = deque()
lenth = 0
while True:
    com_and_value = get_comand().split()

    if com_and_value[0] == 'push':
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
    elif com_and_value[0] == 'pop':
        try:
            print(deq.popleft())
            lenth -= 1
        except:
            print('error')
    elif com_and_value[0] == 'exit':
        print('bye')
        sys.exit()

