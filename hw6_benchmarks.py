def my_buble_sort(il_random, n):

    b_bubl_found = True
    i_buble_element = 0

    while b_bubl_found:
        b_bubl_found = False
        for i in range(0, n-1):
            if il_random[i] > il_random[i + 1]:
                i_buble_element = il_random[i + 1]
                il_random[i + 1] = il_random[i]
                il_random[i] = i_buble_element
                b_bubl_found = True

    return il_random

import random

import datetime


n = 10000
l_rnd_to_cust = []
l_rnd_to_std = []
l_delta_cust = []
l_delta_std = []

#Prepare random numbers list
l_rnd_to_cust = range(0,n)
random.shuffle(l_rnd_to_cust)

l_rnd_to_std = range(0,n)
random.shuffle(l_rnd_to_std)

print('start custom sort')
#print(l_rnd_to_cust)
start = datetime.datetime.now()
my_buble_sort(l_rnd_to_cust, n)
#print(l_rnd_to_cust)
finish = datetime.datetime.now()
l_delta_cust.append(finish - start)
print('start standard sort')
#print(l_rnd_to_std)
start = datetime.datetime.now()
l_rnd_to_std.sort()
#print(l_rnd_to_std)
finish = datetime.datetime.now()
l_delta_std.append(finish - start)


print(l_delta_std)
print(l_delta_cust)
