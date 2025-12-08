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
                case '^': gline.append(-1)
        graph.append(gline)

graph_beam = graph

H = 142
W = 141

col = 0

for i in range(H):
    if i == 0:
        graph_beam[i][init] = 1
        continue

    for j in range(W):
        if graph_beam[i-1][j] > 0:
            if graph_beam[i][j] == -1:
                col += 1
                if (j-1 >= 0):
                    graph_beam[i][j-1] += graph_beam[i-1][j]
                if (j+1 <= W-1):
                    graph_beam[i][j+1] += graph_beam[i-1][j]
            else : #graph_beam[i][j] == 0
                graph_beam[i][j] += graph_beam[i-1][j]

print("Q1:",col)
print("Q2:",sum(graph_beam[-1]))
