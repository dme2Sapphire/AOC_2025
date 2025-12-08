import os
import math

batlines = []
batlinedicts = []
total1 = 0
total2 = 0
with open("input3.txt", "r") as ipt:
    lines = ipt.readlines()
    for line in lines:
        l = line.strip('\n')
        ldict = {}
        for bat in l:
            if bat in ldict:
                ldict[bat] += 1
            else:
                ldict[bat] = 1
        batlinedicts.append(ldict)
        batlines.append(line.strip('\n'))


# print(batlinedicts[1])

def jv_1(line, linedict):
    largest = sorted(linedict.keys())[-1]
    if linedict.get(largest) >= 2:
        return 11*int(largest)
    else:
        resmax = -1
        if line.find(largest) == len(line)-1:
            return 10*int(sorted(linedict.keys())[-2])+int(largest)
        for resbat in line[line.find(largest)+1:]:
            if int(resbat) > resmax:
                resmax = int(resbat)
        return 10*int(largest)+resmax


def first_largest(line_part):
    resmax = -1
    for resbat in line_part:
        if int(resbat) > resmax:
            resmax = int(resbat)
    for idx, resbat in enumerate(line_part):
        if int(resbat) == resmax:
            return (idx, resmax)


def jv_2(line):
    cur_line_part = line
    max_num = 0
    weight = [1e11, 1e10, 1e9, 1e8, 1e7, 1e6, 1e5, 1e4, 1e3, 1e2, 1e1, 1]
    max_n = []
    for i in range(12):
        # print(i)
        # print(cur_line_part)
        # print(first_largest(cur_line_part[:-(12-1-i)]))
        # print(cur_line_part)
        if i == 12-1:
            max_d_idx, max_d = first_largest(cur_line_part[:])
        else:
            max_d_idx, max_d = first_largest(cur_line_part[:-(12-1-i)])
        max_n.append(max_d)
        max_num += max_d*weight[i]
        cur_line_part = cur_line_part[max_d_idx+1:]
    # print(max_n)

    return max_num


for idx, line in enumerate(batlines):

    total1 += jv_1(batlines[idx], batlinedicts[idx])
    total2 += jv_2(batlines[idx])

print("Q1:{}\nQ2:{}".format(total1, total2))
