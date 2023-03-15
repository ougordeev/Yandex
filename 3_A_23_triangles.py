import time

str1 = '10000'


time1 = time.time()
n = int(str1)

ans = 1

for i in range(2,n+1):
    triangles = 0
    for j in range(1,i):
        down = i
        up = down-j
        down_triangles = down - j + 1
        triangles += down_triangles
        if up - j >=0:
            up_triangles = up - j + 1
            triangles += up_triangles
    ans += 1 + triangles
if n == 0:
    print(0)
else:
    print(ans)
print('time1 = ', time.time() - time1)

time2 = time.time()
n = int(str1)

ans = 1
pre_ans = 0

for i in range(2,n+1):
    current = i + 2*ans - pre_ans + (i//2)
    pre_ans = ans
    ans = current
if n == 0:
    print(0)
else:
    print(ans)
print('time2 = ', time.time() - time2)