import time


for k in range(500000,500001):
    str1 = str(k)

    n = int(str1)
    time1 = time.time()

    from collections import deque
    cubes = deque()

    cube_array = []
    i = 2
    while i**3 <= n:
        cubes.append(i**3)
        i += 1
    
    cube_array = []
    
    dp2 = {}
    dp2[0] = 0
    dp2[1] = 1
    dp2[2] = 2
    dp2[3] = 3
    dp2[4] = 4
    dp2[5] = 5
    dp2[6] = 6
    dp2[7] = 7
    cut_cubes = 0
    all_cubes = 1


    for i in range(8,n+1):
        
        if cubes and i == cubes[0]:
            cube_array.append(cubes.popleft())
            cut_cubes += 1
            all_cubes += 1
            half = all_cubes // 2
            if half < cut_cubes - 1:
                cube_array.pop(0)
                cut_cubes -= 1
        variants = []
        for cube in cube_array:
            if i-cube >=0:
                variants.append(dp2[i-cube])
            else:
                break
        dp2[i] = min(variants) + 1
    print(dp2[n])

    print('time 1 = ',time.time() - time1)


    #from collections import deque
    #cubes = deque()
    time2 = time.time()

    cube_array2 = []
    i = 2
    while i**3 <= n:
        cube_array2.append(i**3)
        i += 1
    
    #dp3 = {}
    dp3 = [0] * (n+1)
    dp3[0] = 0
    dp3[1] = 1

    in_cubes = [1]
    j = 2
    ex = 0
    for ocube in cube_array2:
        for i in range(j,ocube):
            minim = 10
            for cube in in_cubes:
                if dp3[i-cube]< minim:
                    minim = dp3[i-cube]
            dp3[i] = minim+1
        in_cubes.append(ocube)
        ex += 1
        if ex == 2:
            ex = 0
            in_cubes.pop(0)
        j = ocube
    for i in range(j,n+1):
            minim = 10
            for cube in in_cubes:
                if dp3[i-cube]< minim:
                    minim = dp3[i-cube]
            dp3[i] = minim+1
    #print(dp3[n])
    print(dp3[-1])

    
    print('time 2 = ',time.time() - time2)


cube_array2 = []
i = 2
while i**3 <= n:
    cube_array2.append(i**3)
    i += 1

dp3 = [0] * (n+1)
dp3[0] = 0
dp3[1] = 1

in_cubes = [1]
j = 2
ex = 0
for ocube in cube_array2:
    for i in range(j,ocube):
        minim = 10
        for cube in in_cubes:
            if dp3[i-cube]< minim:
                minim = dp3[i-cube]
        dp3[i] = minim+1
    in_cubes.append(ocube)
    ex += 1
    if ex == 2:
        ex = 0
        in_cubes.pop(0)
    j = ocube
for i in range(j,n+1):
        minim = 10
        for cube in in_cubes:
            if dp3[i-cube]< minim:
                minim = dp3[i-cube]
        dp3[i] = minim+1
print(dp3[-1])


