# from igraph import *
# import igraph as ig 
import easygraph as eg
# from easygraph.functions.centrality.closeness import closeness_centrality_parallel
# from easygraph.functions.centrality.betweenness import betweenness_centrality_parallel
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

        if file == 'links.txt':
            
            print(f"Profiling dataset {file}")

            print("Profiling loading")
            print("=================")
            print()
            
            
            file = pre_data(filepath, file)
            g = eg.Graph()
            g.add_edges_from_file(file, weighted=False)
            print('*****************************')

            
            worker_list = [4,8,16]
            for n_workers in worker_list:
                print("n_workers=", n_workers)

                print("========clustering=======")
                print("=================")
                print()
                benchmark('eg.clustering(g, n_workers=n_workers)', globals=globals(), n=n)

                print("========hierarchy=======")
                print("=================")
                print()
                benchmark('eg.hierarchy(g, n_workers=n_workers)', globals=globals(), n=n)


                print("========closeness_centrality=======")
                print("=================")
                print()
                benchmark('eg.closeness_centrality(g, n_workers=n_workers)', globals=globals(), n=n)

                print("========betweenness_centrality=======")
                print("=================")
                print()
                benchmark('eg.betweenness_centrality(g, n_workers=n_workers)', globals=globals(), n=n)
        
