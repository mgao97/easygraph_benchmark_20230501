# from igraph import *
import igraph as ig 
import easygraph as eg
from benchmark import benchmark
from easygraph.functions.graph_generator import erdos_renyi_M
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
    np.savetxt('datasets/directed_datasets/'+file, data, fmt='%i')
    return 'datasets/directed_datasets/'+file

if __name__ == "__main__":


    n_sizelist = [10000, 50000, 100000]
    
    for size in n_sizelist:
        if size > 50000:
            m = size * 1.2
        else:
            m = size * 1.5
    
        # =======================EasyGraph=======================
        print(f"Profiling dataset {size}")

        print("Profiling loading")
        print("=================")
        print()

        g = erdos_renyi_M(size, edge=m, directed=False)
        print('*************directed=False****************')
            
        worker_list = [8, 16]
        for n_workers in worker_list:
            print("========betweenness by EasyGraph=======")
            print("n_workers=", n_workers)
            benchmark('eg.hierarchy(g, n_workers=n_workers)', globals=globals(), n=n)
            benchmark('eg.clustering(g, n_workers=n_workers)', globals=globals(), n=n)
            benchmark('eg.closeness_centrality(g, n_workers=n_workers)', globals=globals(), n=n)
            benchmark('eg.betweenness_centrality(g, n_workers=n_workers)', globals=globals(), n=n)

        print(f"Profiling dataset {size}")

        print("Profiling loading")
        print("=================")
        print()

        g1 = erdos_renyi_M(size, edge=m, directed=True)
        print('**************directed=True***************')
            
        worker_list = [4, 8, 16]
        for n_workers in worker_list:
            print("========betweenness by EasyGraph=======")
            print("n_workers=", n_workers)
            benchmark('eg.hierarchy(g1, n_workers=n_workers)', globals=globals(), n=n)
            benchmark('eg.clustering(g1, n_workers=n_workers)', globals=globals(), n=n)
            benchmark('eg.closeness_centrality(g1, n_workers=n_workers)', globals=globals(), n=n)
            benchmark('eg.betweenness_centrality(g1, n_workers=n_workers)', globals=globals(), n=n)
        