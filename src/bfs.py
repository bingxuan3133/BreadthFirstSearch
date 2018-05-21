import networkx as nx
import matplotlib.pyplot as plt
from collections import OrderedDict

"""
class BFS:
    def shortest_path_BFS(self, G=nx.Graph(), source=None, target=None):
        if source not in G or target not in G:
            msg = 'Either source {} or target {} is not in G'
            raise nx.NodeNotFound(msg.format(source, target))

        print("nx.nodes(G): ", nx.nodes(G))
        path = list()
        print("G.adj: ", G.adj)
        path.append(source)
        for adj in G.adj[source]:
            print(adj)
            path.append(adj)
        return path
"""

def BFS(G=nx.Graph(), source=None, depth=None):
    if source not in G:
        msg = 'source {} is not in G'
        raise nx.NodeNotFound(msg.format(source))

    level = list()
    explored = list()
    this_level = list()

    explored.append(source)
    this_level.append(source)

    while this_level.__len__() is not 0:
        level.append(this_level)
        next_level = list()
        for node in this_level:
            for adj_node in G.adj[node]:
                if adj_node not in explored:
                    explored.append(adj_node)
                    next_level.append(adj_node)
        this_level = next_level
        if depth is not None and level.__len__() > depth:
            break

    # convert list to dict
    level = {index: set(nodes) for index, nodes in enumerate(level)}

    return level

def BFS_all(G=nx.Graph(), depth=None):
    pass

def shortest_path_BFS(G=nx.Graph(), source=None, target=None, depth=None):
    if source not in G or target not in G:
        msg = 'either source {} or target {} is not in G'
        raise nx.NodeNotFound(msg.format(source, target))

    level = BFS(G, source, depth)

    if target not in level:
        return Path(False)
    else:
        for this_level, nodes in level:
            if target in nodes:
                return Path(True, this_level)

class Path:
    def __init__(self, reachability, link_required=None):
        self.reachability = reachability
        self.link_required = link_required

def main():
    n = 16
    m = 25
    G = nx.gnm_random_graph(n, m)
    # nx.draw(G, with_labels=True, font_weight='bold')
    nx.draw_spring(G, with_labels=True, font_weight='bold')
    plt.show()

    for node in nx.nodes(G):
        pass