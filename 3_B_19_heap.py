commands = ['0 1', '0 345', '1', '0 4346', '1', '0 2435', '1', '0 235', '0 5', '0 365', '1', '1', '1', '1']
commands.reverse()
def get_comand():
    return commands.pop()

str1 = '2'

heap = []

def insert(heap,x):
    heap.append(x)
    pos = len(heap) - 1
    while pos > 0 and heap[pos] > heap[(pos-1)//2]:
        heap[pos], heap[(pos-1)//2] = heap[(pos-1)//2],heap[pos]
        pos = (pos-1)//2

def extract(heap):
    ans = heap[0]
    heap[0] = heap[-1]
    pos = 0
    while pos*2+2 < len(heap):
        min_son_index = pos*2+1
        if heap[pos*2+2] > heap[min_son_index]:
            min_son_index = pos*2+2
        if heap[pos] < heap[min_son_index]:
            heap[pos], heap[min_son_index] = heap[min_son_index], heap[pos]
            pos = min_son_index
        else:
            break
    heap.pop()
    return(ans)



exit_flag = False
while not exit_flag:
    try:
        com_and_value = get_comand().split()
        if com_and_value[0] == '0':
            try:
                insert(heap, int(com_and_value[1]))
            except:
                print('error')
        else:
            print(extract(heap))
    except:
        exit_flag = True


