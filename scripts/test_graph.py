import networkx as nx
import read_graph as rg

print('TEST RUNNING...')

MG = rg.read('/Users/Admin/Documents/Projects/Kairos/Kairos/graphs/sp_final.gexf')

stops_not_working = []
for n,d in MG.nodes_iter(data=True):
    try:
        d['viagens']
    except:
        stops_not_working.append(n)
stops_not_working.sort()

edges_missing = []
for key in stops_not_working:
    for value in MG.edge[key].values():
        for n_key in value.values():
            edges_missing.append(n_key['attr']['trip_id'])
set(edges_missing)

print('There are {} that do not have viagens info:\n {}'.format(len(stops_not_working), stops_not_working))
print('These are the lines that have those missing info:\n {}'.format(set(edges_missing)))