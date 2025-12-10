
import numpy as np
machines = []
with open("input10.txt", 'r') as ipt:
    for line in ipt.readlines():
        mipt = line.split(' ')
        m_ind = [1 if x == '#' else 0 for x in mipt[0][1:-1]]
        m_opers = [x[1:-1].split(',') for x in mipt[1:-1]]
        for idx, m_oper in enumerate(m_opers):
            m_oper = [int(x) for x in m_oper]
            m_opers[idx] = m_oper
        m_jv = [int(x) for x in (mipt[-1].strip('\n'))[1:-1].split(',')]
        # print(m_opers)
        machines.append({'i_lights': m_ind, 'opers': m_opers, 'jvs': m_jv})
        # print(len(m_ind))

# print(machines[:5])
# maxlen:11 -> 2048 combinations
# mach_num:163


def pos2blist(pos, l):
    blist = [0]*l
    for p in pos:
        blist[p] = 1
    return blist


def blist2num(blist, l):
    w = list(range(l))
    w = [2**x for x in w]
    # print(w)
    # print(blist)
    return sum([a*b for a, b in zip(blist, w)])


def min_press(machine):
    i_lights = machine['i_lights']
    l_num = len(i_lights)
    opers = machine['opers']
    o_num = len(opers)
    opers = np.array([pos2blist(oper, l_num)
                     for oper in opers], np.uint8).T.tolist()

    opers = [blist2num(oper, o_num) for oper in opers]
    o_comb = 2**o_num
    v_comb = [1]*o_comb
    min_press = 99
    min_j = -1
    with open("test_o_10.txt", 'w') as f:
        for j in range(o_comb):
            f.write('--------------------------------\n')
            for idx_l in range(l_num):
                if (bool(int(j & opers[idx_l]).bit_count() % 2) != bool(i_lights[idx_l])):
                    v_comb[j] = 0
                    break
            if v_comb[j] == 1:
                if j.bit_count() < min_press:
                    min_press = j.bit_count()
                    min_j = j

    print(str(bin(min_j))[2:])
    if min_press == 99:
        raise (ValueError(
            f"No solution found,{l_num} Lights, {i_lights}\n {len(machine['opers'])} Operations\n {machine['opers']}"))
    return min_press if min_press != 99 else 0


total_min_press = 0
for idx, machine in enumerate(machines[:]):
    m = min_press(machine)
    total_min_press += m
    print(idx, m)

print(total_min_press)
