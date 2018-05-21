import unittest
import networkx as nx
import matplotlib.pyplot as plt
import bfs

class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_BFS_should_raise_exception(self):
        G = nx.Graph()
        G.add_nodes_from([0, 1])
        G.add_edge(0, 1)
        self.assertRaises(nx.NodeNotFound, bfs.BFS, G, 2)

    def test_BFS_len_2(self):
        G = nx.Graph()
        G.add_nodes_from([0, 1])
        G.add_edge(0, 1)
        expected = {0: {0}, 1: {1}}
        result = bfs.BFS(G, 0)
        self.assertEqual(result, expected)

    def test_BFS_len_5(self):
        G = nx.Graph()
        G.add_nodes_from(range(5))
        H = nx.path_graph(5)
        G.add_edges_from(H.edges)
        expected = {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}}
        result = bfs.BFS(G, 0)
        self.assertEqual(result, expected)

    def test_BFS_len_6(self):
        G = nx.Graph()
        G.add_nodes_from(range(6))
        H = nx.path_graph(6)
        G.add_edges_from(H.edges)
        expected = {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}, 5: {5}}
        result = bfs.BFS(G, 0)
        self.assertEqual(result, expected)

    def test_BFS_len_6_depth_4(self):
        G = nx.Graph()
        G.add_nodes_from(range(6))
        H = nx.path_graph(6)
        G.add_edges_from(H.edges)
        expected = {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}}
        result = bfs.BFS(G, 0, depth=4)
        self.assertEqual(result, expected)

    def test_BFS_random_graph(self):
        n = 16
        m = 25
        G = nx.gnm_random_graph(n, m)
        result = bfs.BFS(G, 0, depth=4)


if __name__ == '__main__':
    unittest.main()