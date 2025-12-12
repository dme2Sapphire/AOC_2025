import numpy as np

nodes_con = []
n_list = []
with open("input11.txt", 'r') as ipt:
    for line in ipt.readlines():
        s_line = line.split(' ')
        n = s_line[0].strip(':')
        nc = [n.strip('\n') for n in s_line[1:]]
        nodes_con.append([n, nc])
        n_list += [s.strip(':').strip('\n') for s in s_line]

node_list = list(set(n_list))
node_list.pop(node_list.index('you'))
node_list.pop(node_list.index('out'))
node_list = sorted(node_list)
node_list = ['you']+node_list+['out']
num_nodes = len(node_list)
# print(num_nodes)
# print(len(nodes_con))

con_matrix = np.zeros((num_nodes, num_nodes))
for n_con in nodes_con:
    for dest in n_con[1]:
        # con_matrix[input,output]
        con_matrix[node_list.index(n_con[0]), node_list.index(dest)] = 1
# print(con_matrix.sum())


# directional
# non-cycle? acyclic
# graph

def conn(node, con_matrix):
    return np.where(con_matrix[node, :])[0].tolist()


def rev_conn(node, con_matrix):
    return np.where(con_matrix[:, node])[0].tolist()


def search_path(node, target, v, con_matrix):
    r = 0
    # print(v)
    if v[target] == 1:
        # print(f'Found Path {np.where(np.array(v))[0].tolist()}')
        return 1

    for n in conn(node, con_matrix):
        # print(f'visit {n}, trace {np.where(np.array(v))[0].tolist()}')
        # print(n)
        if v[n] == 1:
            continue

        else:

            v2 = v.copy()
            v2[n] = 1
            r += search_path(n, target, v2, con_matrix)

    return r


s = search_path(0, num_nodes-1, [0]*num_nodes, con_matrix)
print(f"Q1:{s}")
# print(node_list[506])
# decide score or not


def dec_fullvalid(v):
    return (v[69] and v[105])


def dec_alwaysTrue(v):
    return True

# decide cut or not


def dec_c_touch_out(v):
    return (v[-1])


def dec_c_alwaysFalse(v):
    return False


# def search_path2(node, v, con_matrix, dest, dec, dec_c):
#     r = 0
#     # print(v)
#     if dec_c(v):
#         return 0
#     if v[dest]:
#         print(f'Found Path {np.where(np.array(v))[0].tolist()}')
#         if dec(v):
#             return 1
#         else:
#             return 0

#     for n in conn(node, con_matrix):
#         # print(f'visit {n}, trace {np.where(np.array(v))[0].tolist()}')
#         # print(n)
#         if v[n] == 1:
#             continue

#         else:

#             v2 = v.copy()
#             v2[n] = 1
#             r += search_path2(n, v2, con_matrix, dest, dec, dec_c)

#     return r
# # print(f'{node_list.index('dac')},{node_list.index('fft')}')


def dist_field(node, v, con_matrix, d=0):

    v[node] = d
    # print(v)

    for n in conn(node, con_matrix):
        # print(f'visit {n}, trace {np.where(np.array(v))[0].tolist()}')
        # print(n)

        # v[n] = min(v[n],d+1)
        if v[n] > d+1 or v[n] == 0:
            dist_field(n, v, con_matrix, d+1)
        else:
            v[n] = d+1

    return v


def dist_field_r(node, v, con_matrix, d=0):

    v[node] = d
    # print(v)

    for n in rev_conn(node, con_matrix):
        # print(f'visit {n}, trace {np.where(np.array(v))[0].tolist()}')
        # print(n)

        # v[n] = min(v[n],d+1)
        if v[n] < d-1 or v[n] == 0:
            dist_field_r(n, v, con_matrix, d-1)
        else:
            v[n] = d-1

    return v


def dist_field_full(node, num_nodes, con_matrix):

    pf = dist_field(node, [0]*num_nodes, con_matrix, 0)
    nf = dist_field_r(node, [0]*num_nodes, con_matrix, 0)

    return [p+n for p, n in zip(pf, nf)]


# node_list.index('svr')
# node_list.index('fft')
# node_list.index('dac')
# node_list.index('out')
fftf = dist_field_full(node_list.index('fft'), num_nodes, con_matrix)
dacf = dist_field_full(node_list.index('dac'), num_nodes, con_matrix)
valid_p1 = [d1 <= 0 for d1 in fftf]
valid_p2 = [(d1 > 0 and d2 < 0) for d1, d2 in zip(fftf, dacf)]
valid_p2[node_list.index('dac')] = 1
valid_p2[node_list.index('fft')] = 1
valid_p3 = [d2 >= 0 for d2 in dacf]
# print([(d1>=0 and d2<=0) for d1,d2 in zip(fftf,dacf)]) #fftf->dacf

# print([(d1<=0 and d2>=0) for d1,d2 in zip(fftf,dacf)]) #ALL FALSE
# print(dist_field_full(node_list.index('svr'),num_nodes,con_matrix))
m1 = np.array(valid_p1).reshape((1, -1))
mask1 = m1.T*m1
m2 = np.array(valid_p2).reshape((1, -1))
mask2 = m2.T*m2
m3 = np.array(valid_p3).reshape((1, -1))
mask3 = m3.T*m3

s1 = search_path(node_list.index('svr'), node_list.index(
    'fft'), [0]*num_nodes, con_matrix*mask1)
# print(s1)

s2 = search_path(node_list.index('fft'), node_list.index(
    'dac'), [0]*num_nodes, con_matrix*mask2)
# print(s2)

s3 = search_path(node_list.index('dac'), node_list.index(
    'out'), [0]*num_nodes, con_matrix*mask3)
# print(s3)

print(f"Q2:{s1*s2*s3}")
# def search_path(node,target, v, con_matrix):
#     r = 0
#     # print(v)
#     if v[target] == 1:
#         # print(f'Found Path {np.where(np.array(v))[0].tolist()}')
#         return 1

#     for n in conn(node, con_matrix):
#         # print(f'visit {n}, trace {np.where(np.array(v))[0].tolist()}')
#         # print(n)
#         if v[n] == 1:
#             continue

#         else:

#             v2 = v.copy()
#             v2[n] = 1
#             r += search_path(n,target, v2, con_matrix)

#     return r
