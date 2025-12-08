import math
import itertools

id_ranges = []
ing_ids = []
with open("input5.txt", 'r') as ipt:
    lines = ipt.readlines()
    cur_state = 0
    for line in lines:
        if line == "\n":
            cur_state = 1
            continue

        if cur_state == 0:

            id_range_a = int(line.split('-')[0])
            id_range_b = int(line.split('-')[1])

            # print(math.log10(id_range_a),math.log10(id_range_b))

            id_ranges.append([id_range_a, id_range_b])

        elif cur_state == 1:
            ing_ids.append(int(line))

# print(len(id_ranges), len(ing_ids))
total_1 = 0
for ing_id in ing_ids:
    fresh = 0
    for id_range in id_ranges:
        if (ing_id >= id_range[0] and ing_id <= id_range[1]):
            fresh = 1
            break
    total_1 += fresh

print("Q1:", total_1)

# 好不优雅（（
nodes = list(itertools.chain.from_iterable(id_ranges))
nodes = list(set(nodes))
nodes = sorted(nodes)
gaps = [l-f-1 for l, f in zip(nodes[1:], nodes[:-1])]
# print(gaps[:10])
fresh_gaps = [0]*len(gaps)
for st, ed in id_ranges:
    mode = 0
    for idx, node in enumerate(nodes):
        if st == node:
            mode = 1
        if ed == node:
            mode = 0
        if mode == 1:
            fresh_gaps[idx] = 1


print("Q2:", sum([a*b for a, b in zip(gaps, fresh_gaps)])+len(nodes))

# id_ranges = sorted(id_ranges, key=lambda x: x[0])
