import numpy as np
import math
b = []
with open("input6.txt", "r") as ipt:
    for line in ipt.readlines():
        b.append(list(line.strip('\n')))

b = np.array(b).T
b1 = b[:, :-1].tolist()
b2 = b[:, -1].tolist()
b1 = [''.join(l) for l in b1]
b2 = [l for l in b2 if l != ' ']
print(b2)

q2 = 0
cur = 0
nums = []
for line in b1:
    try:
        nums.append(int(line))
    except Exception as e:
        match b2[cur]:
            case '*': q2 += math.prod(nums)
            case '+': q2 += sum(nums)
        nums = []
        cur += 1
        continue

match b2[cur]:
    case '*': q2 += math.prod(nums)
    case '+': q2 += sum(nums)
nums = []
cur += 1

print("Q2:", q2)
