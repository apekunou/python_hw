l = [1, 5, 8, 2]
l_sum = 0
res = 0
n = len(l)
print("lenght is: {}" .format(n))
while n > 0:
    if n % 2 <> 0:
        l_sum += l[n]
        print(l_sum)
    n -= 1
print("sum is {}" .format(l_sum))
n = len(l)
if n > 0:
    res = l_sum * l[n-1]
print ("res: %s" % res)