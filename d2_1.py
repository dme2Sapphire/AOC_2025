import os
import math

detect_range = []
totalsum = 0
with open("input2.txt", "r") as ipt:
    for detect_range_str in ipt.read().split(","):
        detect_range.append(detect_range_str.split('-'))
# print(detect_range)

# no larger than 2 degree
for range_str in detect_range:
    if ((len(range_str[0]) == len(range_str[1])) and (len(range_str[0]) % 2 == 1)):
        # print("IGNORED:{}".format(range_str))
        totalsum += 0

    else:

        if (len(range_str[0]) % 2 == 1):
            l = len(range_str[1])
            hvl = int(l/2)
            a = ((10**hvl)+1)*10**(hvl-1)
            b = int(range_str[1])
            if int(range_str[1][0:hvl] > range_str[1][hvl:]):
                b = (10**hvl+1)*(int(range_str[1][0:hvl])-1)

        elif (len(range_str[1]) % 2 == 1):
            l = len(range_str[0])
            hvl = int(l/2)
            a = int(range_str[0])
            b = 10**len(range_str[0])-1
            if int(range_str[0][0:hvl] < range_str[0][hvl:]):
                a = (10**hvl+1)*(int(range_str[0][0:hvl])+1)

        else:
            l = len(range_str[0])
            hvl = int(l/2)
            a = int(range_str[0])
            b = int(range_str[1])

            if int(range_str[0][0:hvl] < range_str[0][hvl:]):
                a = (10**hvl+1)*(int(range_str[0][0:hvl])+1)
            if int(range_str[1][0:hvl] > range_str[1][hvl:]):
                b = (10**hvl+1)*(int(range_str[1][0:hvl])-1)

        aprev = a//(10**hvl)
        bprev = b//(10**hvl)
        rangesum = (aprev+bprev)*(bprev-aprev+1)/2*(10**hvl+1)
        totalsum += rangesum
        # print("pre:{},post:{} {},rangesum:{}".format(range_str,a,b,rangesum))

    # print(len(range_str[0]),len(range_str[1]))
        # print(abs(len(range_str[0])-len(range_str[1])))

# for i in range(6,13+1):
#     print(i)
# print(range(6,13))
print("Q1:", totalsum)
