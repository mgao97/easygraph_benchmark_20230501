import igraph as ig 
import easygraph as eg
from benchmark import benchmark
import random


filename_lst = ["undirected_datasets/ca-HepTh.txt",
                "undirected_datasets/email-Enron.txt",
                "undirected_datasets/lastfm_asia_edges.txt",
                "undirected_datasets/ca-HepPh.txt",
                "undirected_datasets/ca-CondMat.txt",                
                ]


lcc_filename_lst = [
    "undirected_datasets/ca-HepTh_lcc.txt",
    "undirected_datasets/email-Enron_lcc.txt",
    "undirected_datasets/lastfm_asia_edges_lcc.txt",
    "undirected_datasets/ca-HepPh_lcc.txt",
    "undirected_datasets/ca-CondMat_lcc.txt"
]

    
# Number of iterations
n = 5
# dataset list
total_filename_lst = filename_lst + lcc_filename_lst

# Random nodes generation
def random_nodes(nodes_num, start_idx, end_idx, seed=3407):
        random.seed(seed)
        node_list = []
        for i in range(nodes_num):
            node_list.append(random.randint(start_idx, end_idx))
        return node_list
    
for i in range(0,len(total_filename_lst)): 
    
    filename=total_filename_lst[i]
    print(f"Profiling dataset {filename}")
    print("Profiling loading")
    print("=================")
    print()
    
    benchmark('eg.GraphC().add_edges_from_file(filename, weighted=False,is_transform=True)', globals=globals(), n=n)

    g = eg.GraphC()
    g.add_edges_from_file(filename, weighted=False,is_transform=True)

    print('*****************************')
    print(len(g.nodes), len(g.edges))


    # node_num: sample node for dijkstra
    node_num = 1000
    start_idx, end_idx = 0, len(g.nodes)-1
    random_node_index_list = random_nodes(node_num, start_idx, end_idx)
    nodes = list(g.nodes)
    eg_node_list = []

    for index in random_node_index_list:
        eg_node_list.append(nodes[index])

    if "lcc" not in filename:
        benchmark('multi_source_dijkstra(g, sources = eg_node_list)', globals=globals(), n=n)
        benchmark('eg.connected_components(g)', globals=globals(), n=n)
        benchmark('eg.k_core(g)', globals=globals(), n=n)
        benchmark('eg.betweenness_centrality(g)', globals=globals(), n=n)
     # We only measure closeness for lcc of each dataset
    benchmark('eg.closeness_centrality(g)', globals=globals(), n=n)
    


    # =======================igraph
    print(f"Profiling dataset {filename}")

    print("Profiling loading")
    print("=================")
    print()
        
    benchmark("ig.Graph.Read_Edgelist(filename,False)", globals=globals(), n=n)
    g= ig.Graph.Read_Edgelist(filename,False)
    print(len(g.vs),len(g.es))
    print("Profiling shortest path")
    print("=======================")
    print()



    ig_node_list = [int(i) for i in eg_node_list]    
    if "lcc" not in filename:
        benchmark("g.distances(source = ig_node_list,weights=[1]*len(g.es))", globals=globals(), n=n)
        benchmark('g.connected_components()', globals=globals(), n=n)
        benchmark('g.coreness()', globals=globals(), n=n)
        benchmark('g.betweenness(directed=False,weights=[1]*len(g.es))', globals=globals(), n=n)
     # We only measure closeness for lcc of each dataset
    benchmark('g.closeness(weights=[1]*len(g.es))', globals=globals(), n=n)
    



   