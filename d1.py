import math

init_pos = 50
cur_pos = init_pos
cross = 0
z_point = 0

def hundred_between(a, b):
    if a > b:
        a, b = b, a
    # a+=10000
    # b+=10000
    return max(0, (math.ceil(b/100)-math.floor(a/100)-1))

with open("input1.txt", 'r') as ipt:
    for line in ipt.readlines():
        rot_dir = line[0]
        num = int(line[1:])
        sign = (1 if rot_dir == 'R' else -1)
        next_pos = cur_pos+sign*num
        # print("Cur_Pos:{},Rotshift:{} {},Dest:{},Cross:{}".format(cur_pos,rot_dir,num,next_pos,hundred_between(cur_pos,next_pos)))
        cross += hundred_between(cur_pos, next_pos)
        cur_pos = (next_pos) % 100
        # cur_pos=(next_pos+10000)%100
        if (cur_pos == 0):
            z_point += 1
            cross += 1

print("Q1:{}\nQ2:{}".format(z_point, cross))
