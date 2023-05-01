# from igraph import *
import igraph as ig 
import easygraph as eg
from easygraph import multi_source_dijkstra
from easygraph.functions.graph_generator import erdos_renyi_P, erdos_renyi_M
from benchmark import benchmark
import sys
import random
import os
import numpy as np
n = 5

def random_nodes(nodes_num, start_idx, end_idx, seed=0):
    random.seed(seed)
    node_list = []
    for i in range(nodes_num):
        node_list.append(random.randint(start_idx, end_idx))
    return node_list



def pre_data(path, file):
    # print(file)
    data = np.loadtxt(path+file,usecols=(0,1))
    np.savetxt('directed_datasets/new_data_'+file, data, fmt='%i')
    return 'directed_datasets/new_data_'+file

if __name__ == "__main__":


    print('for directed networks..............')
    n_sizelist = [10000, 50000, 100000, 200000]
    
    for size in n_sizelist:
        m = size * 2
    
        # =======================EasyGraph=======================
        benchmark('erdos_renyi_M(size, edge=m, directed=False)', globals=globals(), n=n)
        print(f"Profiling dataset {size}")

        print("Profiling loading")
        print("=================")
        print()

        g = erdos_renyi_M(size, edge=m, directed=False).cpp()
        print('*****************************')
        

        print("Profiling shortest path")
        print("=======================")
        print()
        # node_num: sample node for dijkstra
        node_num = 1000
        start_idx, end_idx = 0, len(g.nodes)-1
        random_node_index_list = random_nodes(node_num, start_idx, end_idx)
        nodes = list(g.nodes)
        eg_node_list = []

        for index in random_node_index_list:
            eg_node_list.append(nodes[index])
        print("eg_node_list:",eg_node_list)
        benchmark('multi_source_dijkstra(g, sources = eg_node_list)', globals=globals(), n=n)
        

        # pagerank only apply for directed graph
        # print("Profiling pagerank")
        # print("=======================")
        # print()

        # benchmark('eg.pagerank(g,alpha=0.85)', globals=globals(), n=n)

        print("Profiling k-core")
        print("=======================")
        print()
        benchmark('eg.k_core(g)', globals=globals(), n=n)


        print("Profiling closeness centrality")
        print("=======================")
        print()
        benchmark('eg.closeness_centrality(g)', globals=globals(), n=n)
        


        print("Profiling betweenness centrality")
        print("=======================")
        print()
        benchmark('eg.betweenness_centrality(g)', globals=globals(), n=n)
        
        

        # =======================igraph=======================
        print(f"Profiling dataset {size}")

        print("Profiling loading")
        print("=================")
        print()


        benchmark('ig.Graph().Erdos_Renyi(n=size, m=m, directed=False)', globals=globals(), n=n)
        


        g = ig.Graph().Erdos_Renyi(n=size, m=m, directed=False)
        print(len(g.vs),len(g.es))
        print("Profiling shortest path")
        print("=======================")
        print()

        ig_node_list = [int(i) for i in eg_node_list]
        

        benchmark("g.distances(source = ig_node_list,weights=[1]*len(g.es))", globals=globals(), n=n)

        # pagerank only apply for directed graph
        print("Profiling pagerank")
        print("=======================")
        print()
        benchmark('g.pagerank(damping=0.85)', globals=globals(), n=n)


        print("Profiling k-core")
        print("=======================")
        print()
        benchmark('g.coreness()', globals=globals(), n=n)

        print("Profiling closeness")
        print("=======================")
        print()
        benchmark('g.closeness(weights=[1]*len(g.es))', globals=globals(), n=n)

        print("Profiling betweenness")
        print("=======================")
        print()
        benchmark('g.betweenness(directed=True,weights=[1]*len(g.es))', globals=globals(), n=n)




    
