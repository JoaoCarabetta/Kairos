import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime



def convert_to_minutes(G):

    convert = lambda x: sum([int(y) * (60 - 59 * n) for n, y in enumerate(x.strip("'").split(":"))])

    for i in range(1, len(G) + 1):
        for j in range(len(G.node[i]['t_saida'])):
            G.node[i]['t_saida'][j] = convert(G.node[i]['t_saida'][j])

    return G

G = nx.MultiDiGraph()

# add nodes with atributes
G.add_nodes_from([(1, dict(t_saida=['10:00', '11:00'])),
                  (2, dict(t_saida=['10:15', '11:15'])),
                  (3, dict(t_saida=['10:30', '11:30'])),
                  (4, dict(t_saida=['10:40', '11:40']))])

G = convert_to_minutes(G)

# add edges with attrites
G.add_edges_from([(1, 2, dict(t_dur=10)),
                  (2, 3, dict(t_dur=20)),
                  (3, 4, dict(t_dur=5)),
                  (4, 1, dict(t_dur=15))])




for n1, n2 in G.nodes_iter(data=True):
    print(n1, n2)



"""
plt.figure(figsize=(8,8))
nx.draw(G)
plt.show()
"""