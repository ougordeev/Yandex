str1= '12'
str2 = '5 2 8 10 7 4 25 12 3 1 23 15'

n = int(str1)
heap = list(map(int,str2.split()))
heap_len = n


def extract(heap, heap_len):
    ans = heap[0]
    heap[0] = heap[-1]
    pos = 0
    while pos*2+2 < heap_len:
        min_son_index = pos*2+1
        if heap[pos*2+2] < heap[min_son_index]:
            min_son_index = pos*2+2
        if heap[pos] > heap[min_son_index]:
            heap[pos], heap[min_son_index] = heap[min_son_index], heap[pos]
            pos = min_son_index
        else:
            break
    heap.pop()
    return(ans)

def heapyfy_element(heap,heap_len,index):
    pos = index
    while pos*2+1 < heap_len:
        min_son_index = pos*2+1
        if pos*2+2 < heap_len:
            if heap[pos*2+2] < heap[min_son_index]:
                min_son_index = pos*2+2
        if heap[pos] > heap[min_son_index]:
            heap[pos], heap[min_son_index] = heap[min_son_index], heap[pos]
            pos = min_son_index
        else:
            break

def heapyfy(heap,heap_len):
    max_good_index = heap_len // 2
    for index in range (max_good_index-1,-1,-1):
        heapyfy_element(heap,heap_len,index)

heapyfy(heap, heap_len)

for i in range(n):
    print(extract(heap, heap_len),end=' ')
    heap_len -= 1
print()