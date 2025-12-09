import math
import numpy as np
coord_red = []

with open("input9.txt", 'r') as ipt:
    for line in ipt.readlines():
        coord_red.append([int(line.split(',')[0]), int(line.split(',')[1])])

# print(coord_red)
# print(len(coord_red))
tlen = len(coord_red)
line_border = []


def linedef(coord1, coord2):
    xe = (coord1[0] == coord2[0])
    ye = (coord1[1] == coord2[1])
    if xe:
        return [0, coord1[0], coord1[1], coord2[1]]
    elif ye:
        return [1, coord1[1], coord1[0], coord2[0]]


for idx, coord in enumerate(coord_red):
    if idx == 0:
        l = linedef(coord_red[-1], coord_red[0])
        # print(f'{'x' if l[0] else 'y'}{'+' if (l[3]-l[2] > 0) else '-'}')
        line_border.append(l)
    else:
        l = linedef(coord_red[idx-1], coord_red[idx])
        # print(f'{'x' if l[0] else 'y'}{'+' if (l[3]-l[2] > 0) else '-'}')
        line_border.append(l)


def area_covered(coord1, coord2):
    x = abs(coord1[0]-coord2[0])+1
    y = abs(coord1[1]-coord2[1])+1
    return x*y


def line_cross(l1, l2):
    if l1[0] == l2[0]:
        return False
    if (l1[1]-l2[2])*(l1[1]-l2[3]) < 0 and (l2[1]-l1[2])*(l2[1]-l1[3]) < 0:
        return True
    else:
        return False

# lc=np.zeros((tlen,tlen))
# for i in range(tlen):
#     for j in range(i, tlen):
#         lc[i,j]=line_cross(line_border[i],line_border[j])
#         if lc[i,j]:
#             print(f'Cross of l{i} and l{j} at {'x' if line_border[i][0] else 'y'}{line_border[i][1]},{'x' if line_border[j][0] else 'y'}{line_border[j][1]}')
# print(max(lc.flatten()))
# no intersect..


def ainbc(a, b, c):
    return ((a-b)*(a-c))


def tmpvalid(coord1, coord2, line_border):
    v = True
    x1, y1 = coord1[0], coord1[1]
    x2, y2 = coord2[0], coord2[1]
    rlines = [linedef([x1, y1], [x2, y1]),
              linedef([x2, y1], [x2, y2]),
              linedef([x2, y2], [x1, y2]),
              linedef([x1, y2], [x1, y1])]
    for rline in rlines:
        for bline in line_border:
            if line_cross(rline, bline):
                v = False
                return v
            match bline[0]:
                case 0:
                    if ainbc(bline[1], x1, x2) < 0 and ainbc(bline[2], y1, y2) <= 0 and ainbc(bline[3], y1, y2) <= 0:
                        v = False
                        return v
                case 1:
                    if ainbc(bline[1], y1, y2) < 0 and ainbc(bline[2], x1, x2) <= 0 and ainbc(bline[3], x1, x2) <= 0:
                        v = False
                        return v
    return v


dist = np.zeros((tlen, tlen))

maxa = 0
ai, aj = -1, -1
maxb = 0
bi, bj = -1, -1
for i in range(tlen):
    for j in range(i, tlen):
        dist[i, j] = area_covered(coord_red[i], coord_red[j])
        if dist[i, j] > maxa:
            maxa = dist[i, j]
            ai, aj = i, j
        if dist[i, j] > maxb and tmpvalid(coord_red[i], coord_red[j], line_border):
            maxb = dist[i, j]
            bi, bj = i, j
print("Q1", maxa)
print("Q2", maxb)
print(coord_red[bi], coord_red[bj])
