# 1-x
# 2-1
# 3-1
# 4-2
# 5-1
# 6-3,2     -1
# 7-1
# 8-4
# 9-3
# 10-5,2    -1

import os
import math


def find_invalid_ndigitsegonly_sum(a, b, total, n):

    # print("Original A:{}, B:{}".format(a,b))
    if (a > int(str(a)[:n]*int(total/n))):
        ar = int(str(int(str(a)[:n])+1)*int(total/n))
        if ar > b:
            # print('\n')
            return 0
        # print("REPLACE a {} to {}".format(a,ar))
        a = ar

    if (b < int(str(b)[:n]*int(total/n))):
        br = int(str(int(str(b)[:n])-1)*int(total/n))
        if br < a:
            # print('\n')
            return 0
        # print("REPLACE b {} to {}".format(b,br))
        b = br

    aprev = int(str(a)[:n])
    bprev = int(str(b)[:n])
    mul = int(str(10**(n-1))*int(total/n))/10**(n-1)

    # print("Aprev={},Bprev={},totaldigit={}".format(aprev,bprev,total))
    # print("Sum:{}\n".format((aprev+bprev)*(bprev-aprev+1)/2*mul))
    return (aprev+bprev)*(bprev-aprev+1)/2*mul


detect_ranges = []

with open("input2.txt", "r") as ipt:
    for detect_ranges_str in ipt.read().split(","):
        a = detect_ranges_str.split('-')[0]
        b = detect_ranges_str.split('-')[1]
        if len(b) > len(a):
            detect_ranges.append([int(a), 10**len(a)-1, len(a)])
            detect_ranges.append([10**len(a), int(b), len(a)+1])
        else:
            detect_ranges.append([int(a), int(b), len(a)])

# print(detect_ranges)

totalsum = 0

for detect_range in detect_ranges:
    a = detect_range[0]
    b = detect_range[1]
    d = detect_range[2]
    match d:
        case 1:
            totalsum += 0
        case 2 | 3 | 5 | 7:
            totalsum += find_invalid_ndigitsegonly_sum(a, b, d, 1)
        case 4:
            totalsum += find_invalid_ndigitsegonly_sum(a, b, d, 2)
        case 8:
            totalsum += find_invalid_ndigitsegonly_sum(a, b, d, 4)
        case 6:
            totalsum += find_invalid_ndigitsegonly_sum(a, b, d, 2)
            totalsum += find_invalid_ndigitsegonly_sum(a, b, d, 3)
            totalsum -= find_invalid_ndigitsegonly_sum(a, b, d, 1)
        case 9:
            totalsum += find_invalid_ndigitsegonly_sum(a, b, d, 3)
        case 10:
            totalsum += find_invalid_ndigitsegonly_sum(a, b, d, 2)
            totalsum += find_invalid_ndigitsegonly_sum(a, b, d, 5)
            totalsum -= find_invalid_ndigitsegonly_sum(a, b, d, 1)

print("Final:", totalsum)
