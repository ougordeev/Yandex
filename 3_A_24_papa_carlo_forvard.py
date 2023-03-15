import time
time1 = time.time()

# str1 = '5'
# str2 = ['09:00:00 3600', '13:00:00 1', '13:56:12 1', '13:59:55 1', '14:00:03 14399']

str1 = '2'
str2 = ['09:00:00 3600', '14:00:00 3600']

n = 0
programms_time = []

# with open('06', 'r') as file:
#     n = int(file.readline())
#     for i in range(n):
#         now_programm = file.readline().split()
#         str_time = now_programm[0].split(':')
#         int_time = (int(str_time[0])*60 + int(str_time[1])) * 60 + int(str_time[2]) - 32400

#         speed = int(now_programm[1])
#         programms_time.append((int_time, speed))

n = int(str1)
for i in range(n):
    now_programm = str2[i].split()
    str_time = now_programm[0].split(':')
    int_time = (int(str_time[0])*60 + int(str_time[1])) * 60 + int(str_time[2]) - 32400

    speed = int(now_programm[1])
    programms_time.append((int_time, speed))

start = '09:00:00'
middle_meal = '13:00:00'
start2 = '14:00:00'
home = '18:00:00'

start_split  = start.split(':')
start_seconds = (int(start_split[0])*60 + int(start_split[1])) * 60 + int(start_split[2]) - 32400

middle_split  = middle_meal.split(':')
middle_meal_seconds = (int(middle_split[0])*60 + int(middle_split[1])) * 60 + int(middle_split[2]) - 32400

start2_split  = start2.split(':')
start2_seconds = (int(start2_split[0])*60 + int(start2_split[1])) * 60 + int(start2_split[2]) - 32400

home_split  = home.split(':')
home_seconds = (int(home_split[0])*60 + int(home_split[1])) * 60 + int(home_split[2]) - 32400


programms_time1 = []
programms_time2 = []


for i in range(len(programms_time)):
    if programms_time[i][0] < middle_meal_seconds:
        if i < len(programms_time)-1:
            programms_time1.append((programms_time[i][0],programms_time[i][1], programms_time[i+1][0]))
        else:
            programms_time1.append((programms_time[i][0],programms_time[i][1], home_seconds))
    else:
        if i < len(programms_time)-1:
            programms_time2.append((programms_time[i][0],programms_time[i][1], programms_time[i+1][0]))
    if i == len(programms_time)-1:
        programms_time2.append((programms_time[i][0],programms_time[i][1], home_seconds))
    
time2 = time.time()

dp1 = [0] * (middle_meal_seconds+1)
max_nails = 0
dp1[0] = 0

for programm in programms_time1:
    current_speed = programm[1]
    for i in range(programm[0],min(programm[2]-1,middle_meal_seconds)+1):
        if dp1[i] < max_nails:
            dp1[i] = max_nails
        else:
            max_nails = dp1[i]
        if i+current_speed <= middle_meal_seconds:
            future = dp1[i+current_speed]
            if dp1[i]+1 > future:
                dp1[i+current_speed] = dp1[i]+1

if dp1[middle_meal_seconds] > max_nails:
    max_nails = dp1[middle_meal_seconds]

while programms_time2 and programms_time2[0][2] < start2_seconds:
        programm = programms_time2.pop(0)

dp2 = [0] * (home_seconds - start2_seconds+1)
dp2[0] = max_nails

for programm in programms_time2:
    current_speed = programm[1]
    for i in range(max(0, programm[0] - start2_seconds), programm[2] - start2_seconds):
        if dp2[i] < max_nails:
            dp2[i] = max_nails
        else:
            max_nails = dp2[i]
        if i+current_speed <= home_seconds - start2_seconds:
            future = dp2[i+current_speed]
            if dp2[i]+1 > future:
                dp2[i+current_speed] = dp2[i]+1

if dp2[home_seconds-start2_seconds] > max_nails:
    max_nails = dp2[home_seconds-start2_seconds]

print(max_nails)
print('time1 = ', time2 - time1)
print('time2 = ', time.time() - time2)

    
