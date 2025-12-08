import numpy as np
import math

coord = []
with open("input8.txt", 'r') as ipt:
    for line in ipt.readlines():
        coord.append([int(axis) for axis in line.split(',')])

TOTAL_BOX = 1000
dist_matrix = np.ones((TOTAL_BOX, TOTAL_BOX))*1e10
for i in range(TOTAL_BOX):
    for j in range(i, TOTAL_BOX):
        dist_matrix[i, j] = math.dist(coord[i], coord[j])
    dist_matrix[i, i] = 1e10

dist_flatten = dist_matrix.flatten()
idx = dist_flatten.argsort()[:]
xy = np.unravel_index(idx, (TOTAL_BOX, TOTAL_BOX))
# print(xy,dist_flatten[idx])


class Dsu:
    def __init__(self, size):
        self.pa = list(range(size))
        self.size = [1]*size
        self.conn = 0
        self.counter = 0

    def conn(self):
        return self.conn

    def counter(self):
        return self.counter

    def find(self, x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]

    def unite(self, x, y):
        initx = x
        inity = y
        x, y = self.find(x), self.find(y)
        if x == y:
            self.counter += 1
            # print('skip')
            return -1, -1
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.pa[y] = x
        self.size[x] += self.size[y]
        self.conn += 1
        # if self.conn==999:
        #     print("ALL CONNECTED, LAST TWO:{} and {}".format(initx,inity))
        self.counter += 1
        return initx, inity


conn = 0
boxcon = Dsu(1000)

while (boxcon.conn < 999):
    if boxcon.counter == 999:
        print("Q1:", math.prod(sorted(boxcon.size, reverse=True)[:3]))
    boxn1, boxn2 = boxcon.unite(xy[0][boxcon.counter], xy[1][boxcon.counter])

print("Q2:", coord[boxn1][0]*coord[boxn2][0])
