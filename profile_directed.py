import igraph as ig 
import easygraph as eg
from benchmark import benchmark
import random

filename_lst = [

                "directed_dataset/amazon0302.txt",
                 "directed_dataset/web-NotreDame.txt",
                 "directed_dataset/soc-Slashdot0811.txt",
                "directed_dataset/email-EuAll.txt",
                "directed_dataset/soc-Epinions1.txt",
                "directed_dataset/pgp.edgelist",
                "directed_dataset/wiki-Vote.txt",
              "directed_dataset/p2p-Gnutella04.txt",
               
                ]
lcc_filename_lst=[
    'directed_dataset/soc-Epinions1_lcc.txt',
    'directed_dataset/pgp_lcc.edgelist',
    'directed_dataset/wiki-Vote_lcc.txt',
    'directed_dataset/p2p-Gnutella04_lcc.txt',
    'directed_dataset/amazon0302_lcc.txt',
    'directed_dataset/web-NotreDame_lcc.txt',
    'directed_dataset/email-EuAll_lcc.txt',
    'directed_dataset/soc-Slashdot0811_lcc.txt',
]
# Number of iterations
n = 3
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
    filename = total_filename_lst[i]

    print(f"Profiling dataset {filename}")

    print("Profiling loading")
    print("=================")
    print()

    
    benchmark('eg.DiGraphC().add_edges_from_file(filename, weighted=False,is_transform=True)', globals=globals(), n=n)

    g = eg.DiGraphC()
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
        benchmark('eg.strongly_connected_components(g)', globals=globals(), n=n)
        benchmark('eg.k_core(g)', globals=globals(), n=n)
        benchmark('eg.pagerank(g,alpha=0.85)', globals=globals(), n=n)
        benchmark('eg.betweenness_centrality(g)', globals=globals(), n=n)
        
    # We only measure closeness for lcc of each dataset
    benchmark('eg.closeness_centrality(g,sources = eg_node_list)', globals=globals(), n=n)
    


    # =======================igraph
    print(f"Profiling dataset {filename}")

    print("Profiling loading")
    print("=================")
    print()

    benchmark("ig.Graph.Read_Edgelist(filename,True)", globals=globals(), n=n)
    g= ig.Graph.Read_Edgelist(filename,True)
    print(len(g.vs),len(g.es))



    ig_node_list = [int(i) for i in eg_node_list]

   

    if "lcc" not in filename:
        benchmark("g.distances(source = ig_node_list,weights=[1]*len(g.es))", globals=globals(), n=n)
        benchmark('g.connected_components()', globals=globals(), n=n)
        benchmark('g.coreness()', globals=globals(), n=n)
        benchmark('g.pagerank(damping=0.85)', globals=globals(), n=n)
        benchmark('g.betweenness(directed=False,weights=[1]*len(g.es))', globals=globals(), n=n)
    benchmark('g.closeness(vertices=ig_node_list,weights=[1]*len(g.es))', globals=globals(), n=n)
    
    
