import numpy as np
import math
a = []

with open("input6.txt", "r") as ipt:
    for line in ipt.readlines():
        a.append([x.strip('\n')
                 for x in line.split(' ') if (x != '' and x != '\n')])

a = np.array(a).T.tolist()

# print(a[:10])

q1 = 0
for p in a:
    pb = [int(x) for x in p[:-1]]
    match p[-1]:
        case '*':
            q1 += math.prod(pb)
        case '+':
            q1 += sum(pb)
print("Q1:", q1)
