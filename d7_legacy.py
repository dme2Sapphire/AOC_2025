import numpy as np

graph = []

with open("input7.txt", 'r') as ipt:
    for line in ipt.readlines():
        gline = []
        for idx, char in enumerate(line):
            match char:
                case '.':  gline.append(0)
                case 'S':
                    gline.append(0)
                    init = idx
                case '^': gline.append(1)
        graph.append(gline)

graph_np = np.array(graph)
graph_np_beam = np.copy(graph_np)

# print(init)
# print(graph_np[:10,60:80]) 142*141
H = 142
W = 141
col = 0

for i in range(H):
    if i == 0:
        graph_np_beam[i, init] = 2
        continue

    for j in range(W):
        # print(i)
        if graph_np_beam[i-1, j] == 2:
            if graph_np_beam[i, j] == 1:
                col += 1
                if (j-1 >= 0):
                    graph_np_beam[i, j-1] = 2
                if (j+1 <= W-1):
                    graph_np_beam[i, j+1] = 2
            elif graph_np_beam[i, j] == 0:
                graph_np_beam[i, j] = 2

print("Q1:",col)


with open("out7.txt", 'w') as f:
    f.write(str(graph_np_beam.tolist()))
