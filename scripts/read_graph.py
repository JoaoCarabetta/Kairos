import ast
import networkx as nx

def read(path):

    MG = nx.read_gexf(path)

    for node in MG.nodes(data=True):
        for key, value in MG.edge[node[0]].items():
            for k, v in value.items():
                if type(v['attr']) == str:
                    MG.edge[node[0]][key][k]['attr'] = ast.literal_eval(v['attr'])

    for node in MG.nodes(data=True):
        if isinstance(MG.node[node[0]]['location'], str):
            MG.node[node[0]]['location'] = ast.literal_eval(MG.node[node[0]]['location'])
        if len(node[1]) == 3:
            if type(MG.node[node[0]]['viagens']) == str:
                MG.node[node[0]]['viagens'] = ast.literal_eval(MG.node[node[0]]['viagens'])

    return MG