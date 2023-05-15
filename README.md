# EasyGraph_benchmark_20230501
This repository mainly includes source code for benchmarking the performance of EasyGraph with hybrid programming and multiprocessing techniques. 


- [easygraph-bench](#EasyGraph-bench)
  
  - [Objectives](#objectives)
  
    - [Objective 1](#for-objective-1)
    - [Objective 2](#for-objective-2)
    
  - [Benchmarked methods](#benchmarked-methods)
    
    - [For Objective 1](#for-objective-1)
    - [For Objective 2](#for-objective-2)
    
  - [Run](#run)
    
    - [Run locally](#run-locally)
      - [Prerequisites](#prerequisites)
      - [Setting](#setting)
      - [Scripts usage](#scripts-usage)
    
  - [Result visualization ](#result-visualization-for-objective-1-only)
  
    

## Objectives

### Objective 1

Benchmarking code that compares the performance of EasyGraph with hybrid programming. Specifically, we compare [EasyGraph](https://github.com/easy-graph/Easy-Graph) (with C++ binding) with the [igraph](https://github.com/igraph/python-igraph) library.

For different types of networks, we compare a series of network analysis functions including:


|     Undirected Network       |      Directed Network      |
| :--------------------------: |:--------------------------:|
|       Network Loading        |      Network Loading       |
|      the Shortest Path       |     the Shortest Path      |
|    the K-core Centrality     |   the K-core Centrality    |
|   the Closeness Centrality   |  the Closeness Centrality  |
|  the Betweenness Centrality  | the Betweenness Centrality |
|              /               |  the PageRank Centrality   |


The PageRank centrality is not suitable for undirected networks.
### Objective 2

Benchmarking code that compares the performance of multiprocessing techniques used in EasyGraph.

For different types of networks, we compare a series of network analysis functions including:

|      Undirected Network        |        Directed Network         |
| :----------------------------: | :-----------------------------: |
|  the Local Cluster Coefficient |  the Local Cluster Coefficient  |
|         the Hierarchy          |          the Hierarchy          |
|    the Closeness Centrality    |     the Closeness Centrality    |
|   the Betweenness Centrality   |     the Betweenness Centrality  |


## Benchmarked methods

### For Objective 1

We compare EasyGraph (with C++ binding) with the igraph library. 

The specific way the function is called is shown in the following file



```  EasyGraph(version:0.2a47): 
  '"import easygraph as eg"'
  loading(undirected): "'eg.GraphC().add_edges_from_file(filename, weighted=False,is_transform=True)'"
  loading(directed): "'eg.DiGraphC().add_edges_from_file(filename, weighted=False,is_transform=True)'"
  pagerank: "'eg.pagerank(g,alpha=0.85)'"
  shortest path: "'eg.multi_source_dijkstra(g, sources = eg_node_list)'"
  connected_components(undirected): "'eg.connected_components(g)'"
  connected_components(directed): "'eg.strongly_connected_components(g)'"
  closeness: "'eg.closeness_centrality(g, sources = eg_node_list)'"
  betweenness: "'eg.betweenness_centrality(g)'"
  k-core: "'eg.k_core(g)'"```


  '"import igraph as ig"'
  igraph(version:0.10.4):
  loading(undirected): "'ig.Graph.Read_Edgelist(filename, False)'"
  loading(directed): '"ig.Graph.Read_Edgelist(filename, True)"'
  pagerank: '"g.pagerank(damping=0.85)"'
  shortest path: '"g.distances(source = ig_node_list,weights=[1]*len(g.es))"'
  connected components: '"g.connected_components()"'
  k-core: '"g.coreness()"'
  closeness: '"g.closeness_centrality(g, weights=[1]*len(g.es), sources = ig_node_list)"'
  betweenness(directed): '"g.betweenness(directed=True, weights=[1]*len(g.es))"'
  betweenness(undirected): "'g.betweenness(directed=False, weights=[1]*len(g.es))'"

```

### For Objective 2

We compare EasyGraph with the different numbers of workers. 

The specific way the function is called is shown in the following file



```  EasyGraph(version:0.2a47): 
  '"import easygraph as eg"'
  loading(undirected): "'g = erdos_renyi_M(size, edge=m, directed=False)'"
  loading(directed): "'g = erdos_renyi_M(size, edge=m, directed=True)'"
  hierarchy: "'eg.hierarchy(g, n_workers=n_workers)'"
  clustering: "'eg.clustering(g, n_workers=n_workers)'"
  closeness: "'eg.closeness_centrality(g, sources = eg_node_list)'"
  betweenness: "'eg.betweenness_centrality(g)'"

```




## Run

### Run locally

#### Prerequisites

`3.9 <= python <= 3.10` is required.

First, to run these scripts, you need to clone the repo.

To install `EasyGraph`:

Installation with pip

```bash
pip install Python-EasyGraph
```

Install from scratch

You will need to build EasyGraph wheels from scratch if your platform does not support them. Please run the following code to install the module.

```bash
git clone https://github.com/easy-graph/Easy-Graph && cd Easy-Graph && git checkout pybind11
pip install pybind11
python3 setup.py build_ext
python3 setup.py install
```

To install the igraph library, please refer to https://python.igraph.org/en/stable/

#### Setting

**For objective1:** 

Iteration:  3 times for directed network datasets, 5 times for undirected network datasets.

Node sample: 1,000 nodes are sampled from directed network datasets when testing the algorithm of identification of the shortest paths and the metric of closeness centrality.

 Subgraph generation: the largest connected components/strongly connected components are calculated by NetworkX, code is presented in get_lcc_edgelist.py

**For objective2:**

Iteration:  3 times for directed network datasets, 5 times for undirected network datasets.

Node sample: 1,000 nodes are sampled from directed network datasets when testing the algorithm of the identification of the shortest paths and the metric of closeness centrality.

 Subgraph generation: the largest connected components/strongly connected components are calculated by NetworkX, code is presented in get_lcc_edgelist.py

#### Scripts usage
```
cd easygraph_benchmark_20230501

```

There are the following scripts in this directory：

```
benchmark.py // tool for calculating the time consumption of each function
get_lcc_edgelist.py // tool for getting the largest connected components of each dataset
profile_directed_hp_er.py // bench on directed random networks generated by Erdős-Renyi random network model with hybrid programming
profile_directed_hp_rw.py // bench on directed real-world networks generated by Erdős-Renyi random network model with hybrid programming
profile_directed_mp_rw.py // bench on directed real-world networks with multiprocessing techniques
profile_directed_mp_er.py // bench on directed random networks generated by Erdős-Renyi random network model with multiprocessing techniques
profile_undirected_hp_er.py // bench on undirected random networks generated by Erdős-Renyi random network model with hybrid programming
profile_undirected_hp_rw.py // bench on undirected real-world networks with hybrid programming 
profile_undirected_mp_rw.py // bench on undirected real-world networks with multiprocessing techniques

```

1. Open your terminal, and make sure you have entered into the right Python environment that is equipped with EasyGraph and the igraph library. 
2. Choose a script and run the script as follows：

```
python profile_directed_hp_rw.py
```




## Datasets


The `er_*` Erdos-Renyi random graphs are generated with `eg.erdos_renyi_M()` with artificially defined numbers of nodes and edges.

<!-- BEGIN DATASET TABLE -->

| Dataset Name                                                 | nodes   | edges   | is_directed | average_degree | density  |
| ------------------------------------------------------------ | ------- | ------- | ----------- | -------------- | -------- |
| ER\_10k\_u                                                   | 10,000  | 20,000  | False       | 4.0            | 5.0e-05  |
| ER\_50k\_u                                                   | 50,000 | 100,000 | False       | 4.0            | 1.0e-05  |
| ER_100k_u                                                    | 100,000 | 200,000 | False       | 4.0            | 5.0e-06  |
| ER_200k_u                                                    | 200,000 | 400,000 | False       | 4.0            | 2.5e-06  |
| ER_10k_d                                                     | 10,000  | 20,000  | True        | 4.0            | 2.5e-05  |
| ER_50k_d                                                     | 50,000  | 100,000  | True        | 4.0            | 5.0e-06  |
| ER_100k_d                                                    | 100,000 | 200,000 | True        | 4.0            | 2.5e-06  |
| ER_200k_d                                                    | 200,000 | 400,000 | True        | 4.0            | 1.25e-06 |
| [ca-HepTh](http://snap.stanford.edu/data/ca-HepTh.html)      | 9,877    | 25,998   | False       | 5.26           | 0.0005   |
| [email-Enron](http://snap.stanford.edu/data/email-Enron.html) | 36,692   | 183,831  | False       | 10.02          | 0.0003   |
| [ca-HepPh](http://snap.stanford.edu/data/ca-HepPh.html)      | 12,008   | 118,521  | False       | 19.74          | 0.0016   |
| [ca-CondMat](http://snap.stanford.edu/data/ca-CondMat.html)  | 23,133   | 93,497   | False       | 8.08           | 0.0003   |
| [amazon0302](http://snap.stanford.edu/data/amazon0302.html)  | 262,111  | 1,234,877 | True        | 9.42           | 1.79e-05 |
| [soc-Epinions1](http://snap.stanford.edu/data/soc-Epinions1.html) | 75,879   | 508,837  | True        | 13.41          | 8.8e−05  |
| [wikivote](http://snap.stanford.edu/data/wiki-Vote.html)     | 7,115    | 103,689  | True        | 29.15          | 0.0020   |
| pgp.edgelist                                                 | 39,796   | 301,498  | True        | 15.15          | 0.0002   |
| [p2p-Gnutella04](http://snap.stanford.edu/data/p2p-Gnutella04.html) | 10,876   | 39,994   | True        | 7.35           | 0.0003   |
| [soc-Slashdot0811](http://snap.stanford.edu/data/soc-Slashdot0811.html) | 77,360   | 905,468  | True        | 23.41          | 0.0002   |
| [web-NotreDame](http://snap.stanford.edu/data/web-NotreDame.html) | 325,729  | 1,497,134 | True        | 9.19           | 1.5e−07  |
| [email-EuAll](http://snap.stanford.edu/data/email-Enron.html) | 265,214  | 420,045  | True        | 3.17           | 0.0003   |

