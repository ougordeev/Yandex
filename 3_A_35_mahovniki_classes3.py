from threading import stack_size
from sys import setrecursionlimit
setrecursionlimit (1000000)
stack_size(134217728)
import heapq

import time
time1 = time.time()

# with open('02_35', 'r') as file:
#     n = int(file.readline())


    # classes_need = [0]*(n+1)
    # classes_need[0] = n+1
    # classes = [0]*(n+1)
    # for i in range(1,n+1):
    #     current = file.readline()
    #     if current[0] == '0':
    #         current_class = frozenset()
    #     else:
    #         current_class = frozenset(map(int,current.split()[1:]))
    #     classes[i] = current_class
    #     for element in current_class:
    #         classes_need[element] +=1

str1 = '6'
str2 = ['1 2','0','1 2','3 1 2 5','1 2','4 1 3 4 5']

n = int(str1)
classes = [0]*(n+1)
classes_need = [0]*(n+1)
classes_need[0] = n+1

for i in range(1,n+1):
    current = str2[i-1]
    if current[0] == '0':
        current_class = frozenset()
    else:
        current_class = frozenset(map(int,current.split()[1:]))
    classes[i] = current_class
    for element in current_class:
        classes_need[element] +=1

numbers_heap = []
for i in range(1,n+1):
    if classes_need[i] == 0:
        numbers_heap.append(-i)

heapq.heapify(numbers_heap)
sort = [0]*n
j = n-1
while numbers_heap:
    element = -heapq.heappop(numbers_heap)
    sort[j] = element
    j -=1
    for vay in classes[element]:
        old = classes_need[vay]
        new = old - 1
        classes_need[vay] = new
        if new == 0:
            heapq.heappush(numbers_heap,-vay)

print(' '.join(map(str,sort)))  
print('time1 = ', time.time() - time1)



