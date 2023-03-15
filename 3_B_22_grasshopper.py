str1 = '8 3'
n,k = map(int,str1.split())

hop_list = [0] * (n)
hop_list[0] = 1
for i in range(1,n):
    sum = 0
    for j in range(i-1,i-k-1,-1):
        if j >= 0:
            sum += hop_list[j]
        else:
            break
    hop_list[i] = sum
print(hop_list[-1])