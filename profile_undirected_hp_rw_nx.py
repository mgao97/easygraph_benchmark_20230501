# import igraph as ig 
import easygraph as eg
from benchmark import benchmark
import random
import numpy as np
import os
import networkx as nx

n = 5


# Random nodes generation
def random_nodes(nodes_num, start_idx, end_idx, seed=3407):
        random.seed(seed)
        node_list = []
        for i in range(nodes_num):
            node_list.append(random.randint(start_idx, end_idx))
        return node_list

def pre_data(path, file):
    # print(file)
    data = np.loadtxt(path+file,usecols=(0,1))
    np.savetxt(path+file, data, fmt='%i')
    return path+file


if __name__ == "__main__":


    print('for undirected networks..............')
    filepath = 'datasets/undirected_datasets/'
    filelist = os.listdir(filepath)
    print(filelist)
    for file in filelist:
        if file == '.DS_Store':
            continue
        
        # =======================EasyGraph=======================
        filename = filepath + file    
        print(f"Profiling dataset {file}")

        print("Profileing loading")
        print("=================")
        print()
        benchmark('nx.Graph().add_edges_from_file(filename)', globals=globals(), n=n)

        g = nx.Graph()
        g.add_edges_from_file(filename)

        # node_num: sample node for dijkstra
        node_num = 1000
        start_idx, end_idx = 0, len(g.nodes)-1
        random_node_index_list = random_nodes(node_num, start_idx, end_idx)
        nodes = list(g.nodes)
        nx_node_list = []

        for index in random_node_index_list:
            nx_node_list.append(nodes[index])

        if "_lcc" not in file:
            print("Profiling shortest path")
            print("=======================")
            print()
            benchmark('nx.shortest_path(g, sources = nx_node_list)', globals=globals(), n=n)

            print("========k-core=======")
            print("=================")
            print()
            benchmark('nx.core_number(g)', globals=globals(), n=n)

            print("========betweenness_centrality=======")
            print("=================")
            print()
            benchmark('nx.betweenness_centrality(g)', globals=globals(), n=n)
        # since igraph only supports the metric of closeness centrality for lcc of each dataset, we choose the same for fair comparison
        print("========closeness_centrality=======")
        print("=================")
        print()
        benchmark('nx.closeness_centrality(g)', globals=globals(), n=n)
        

        
        # print("Profiling loading")
        # print("=================")
        # print()
        # benchmark('eg.GraphC().add_edges_from_file(filename, weighted=False,is_transform=True)', globals=globals(), n=n)

        # g = eg.GraphC()
        # g.add_edges_from_file(filename, weighted=False,is_transform=True)


        # # node_num: sample node for dijkstra
        # node_num = 1000
        # start_idx, end_idx = 0, len(g.nodes)-1
        # random_node_index_list = random_nodes(node_num, start_idx, end_idx)
        # nodes = list(g.nodes)
        # eg_node_list = []

        # for index in random_node_index_list:
        #     eg_node_list.append(nodes[index])

        # if "_lcc" not in file:
        #     print("Profiling shortest path")
        #     print("=======================")
        #     print()
        #     benchmark('eg.multi_source_dijkstra(g, sources = eg_node_list)', globals=globals(), n=n)

        #     print("========k-core=======")
        #     print("=================")
        #     print()
        #     benchmark('eg.k_core(g)', globals=globals(), n=n)

        #     print("========betweenness_centrality=======")
        #     print("=================")
        #     print()
        #     benchmark('eg.betweenness_centrality(g)', globals=globals(), n=n)
        # # since igraph only supports the metric of closeness centrality for lcc of each dataset, we choose the same for fair comparison
        # print("========closeness_centrality=======")
        # print("=================")
        # print()
        # benchmark('eg.closeness_centrality(g)', globals=globals(), n=n)
        


        # # =======================igraph=======================
        # print(f"Profiling dataset {file}")

        # print("Profiling loading")
        # print("=================")
        # print()
            
        # benchmark("ig.Graph.Read_Edgelist(filename,False)", globals=globals(), n=n)
        # g= ig.Graph.Read_Edgelist(filename,False)
        


        # ig_node_list = [int(i) for i in eg_node_list]    
        # if "_lcc" not in file:
        #     print("Profiling shortest path")
        #     print("=======================")
        #     print()
        #     benchmark("g.distances(source = ig_node_list,weights=[1]*len(g.es))", globals=globals(), n=n)
        #     print("========k-core=======")
        #     print("=================")
        #     print()
        #     benchmark('g.coreness()', globals=globals(), n=n)
        #     print("========betweenness_centrality=======")
        #     print("=================")
        #     print()
        #     benchmark('g.betweenness(directed=False,weights=[1]*len(g.es))', globals=globals(), n=n)
        # # We only measure closeness for lcc of each dataset
        # print("========closeness_centrality=======")
        # print("=================")
        # print()
        # benchmark('g.closeness(weights=[1]*len(g.es))', globals=globals(), n=n)
    