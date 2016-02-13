i_dist = 0
f_petrol = 0.0
i_sum = 0
i = 0
for line in open('C:\Python study\car_stats.csv'):
#    print(line)
    if i == 0:
        i = i + 1
        continue
    else: i = i + 1
    l_data = line.split(',')
    print(l_data)
    if l_data[1] <> '':
        i_dist = int(l_data[1])
    if l_data[2] <> '':
        f_petrol = f_petrol + float(l_data[2])
    if l_data[5] == 'BYR':
        i_sum = i_sum + int(l_data[4])

print(i_dist)
print(f_petrol)
print(i_sum)