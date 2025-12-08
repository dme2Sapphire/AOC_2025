import cv2
import numpy as np

proll_matrix = []

with open("input4.txt", "r") as ipt:
    lines = ipt.readlines()
    for line in lines:
        proll_line = []
        for chr in line:
            if chr == '.':
                proll_line.append(0)
            elif chr == '@':
                proll_line.append(1)
        proll_matrix.append(proll_line)

proll_np_matrix = np.array(proll_matrix, np.uint8)

kernel_1 = np.array([[1, 1, 1],
                     [1, 0, 1],
                     [1, 1, 1]], np.uint8)


test = cv2.filter2D(proll_np_matrix, -1, kernel_1,
                    borderType=cv2.BORDER_CONSTANT)
init_roll_num = proll_np_matrix.flatten().sum()
# print(test.shape)
# print(test[:10,:10])
print("Q1:{}".format(((test < 4)*proll_np_matrix).flatten().sum()))

cur_matrix = proll_np_matrix
while True:

    keep_matrix = (cv2.filter2D(cur_matrix, -1, kernel_1,
                   borderType=cv2.BORDER_CONSTANT) >= 4)
    next_matrix = cur_matrix*keep_matrix
    if (np.array_equal(next_matrix, cur_matrix)):
        break
    cur_matrix = next_matrix

print("Q2:{}".format(init_roll_num-cur_matrix.flatten().sum()))
