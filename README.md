# easygraph_benchmark_20230501
This repository mainly includes code for benchmarking the performance of graph libraries including easygraph and igraph.


- [easygraph-bench](#easygraph-bench)
  
  - [Objectives](#objectives)
  
    - [Objective 1](#for-objective-1)
    - [Objective 2](#for-objective-2)
  
  - [Benchmarking method](#benchmarking-method)
  
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

Benchmarking code that compares the performance of the 2 graph libraries [easygraph](https://github.com/easy-graph/Easy-Graph) (with C++ binding) and [igraph](https://github.com/igraph/python-igraph).

For different type graph, we compare :

|   Undirected Graph   |        Directed Graph         |
| :------------------: | :---------------------------: |
|    shortest path     |         shortest path         |
|        k-core        |            k-core             |
|      closeness       |           closeness           |
|     betweenness      |          betweenness          |
| connected components | strongly_connected_components |
|          /           |           page rank           |

### Objective 2

Benchmarking code that compares the performance of multi-process in different easygraph functions

(continue....)



## Benchmarking method

[timeit.Timer.autorange](https://docs.python.org/3.10/library/timeit.html#timeit.Timer.autorange) is used to run the specified methods on the graph objects.

If the method returns a Generator, the result will be exhausted.

See [get_Timer_args()](https://github.com/tddschn/easygraph-bench/blob/69cc89889e39386f495b7fa07be3116443cc9356/utils.py#L191) for more details.

## Benchmarked methods

### For Objective 1

We compare our methods (with C++ binding) with igraph. 

The specific way the function is called is shown in the following .yml file

  ```yaml

  easygraph(version:0.2a47):
  	'"import easygraph as eg'"
  	loading(undirected): "'eg.GraphC().add_edges_from_file(filename, weighted=False,is_transform=True)'"
    loading(directed): "'eg.DiGraphC().add_edges_from_file(filename, weighted=False,is_transform=True)'"
    pagerank: "'eg.pagerank(g,alpha=0.85)'"
    shortest path: "'eg.multi_source_dijkstra(g, sources = eg_node_list)'"
    connected_components(undirected): '"eg.connected_components(g)'"
   	connected_components(directed): '"eg.strongly_connected_components(g)'"
   	closeness: '"eg.closeness_centrality(g, sources = eg_node_list)'"
   	betweenness: '"eg.betweenness_centrality(g)'"
   	k-core: '"eg.k_core(g)'"
   
 
    igraph(version:0.10.4):
    loading(undirected): "'ig.Graph.Read_Edgelist(filename, False)'"
    loading(directed): '"ig.Graph.Read_Edgelist(filename, True)"'
    pagerank: '"g.pagerank(damping=0.85)"'
    shortest path: '"g.distances(source = ig_node_list,weights=[1]*len(g.es))"'
    connected components: '"g.connected_components()"'
    k-core: '"g.coreness()"'
    closeness: '"g.closeness_centrality(g, weights=[1]*len(g.es), sources = ig_node_list)'"
   	betweenness(directed): '"g.betweenness(directed=True, weights=[1]*len(g.es))'"
   	betweenness(undirected): '"g.betweenness(directed=False, weights=[1]*len(g.es))'"


    
  ```

### For Objective 2

(Continue..)




## Run

### Run locally

#### Prerequisites

`3.9 <= python <= 3.10` is required.

First, to run these scripts, you need to clone the repo.

To install `easygraph`:  
As of 5/1/2023, wheel for `python-easygraph` is not available on PyPI, and you need to build it yourself and install the module by running the following code.

```bash
git clone https://github.com/easy-graph/Easy-Graph && cd Easy-Graph && git checkout pybind11
pip install pybind11
python3 setup.py install
```

To install igraph, please refer to https://python.igraph.org/en/stable/

#### Setting

**For objective1:** 

Iteration:  3 times for directed graph datasets, 5 times for undirected graph datasets.

Node sample: 1000 nodes are sampled from directed graph datasets when test shortest path and closeness.

 Subgraph generation: largest connected components/strongly connected components are calculated by NetworkX, code is presented in get_lcc_edgelist.py

**For objective2:**

(continue...) 

#### Scripts usage

cd easygraph_benchmark_20230501

There are following scripts in this directory：

```
benchmark.py  // tool for calculating the time consumption of each function
get_lcc_edgelist.py // tool for getting largest connnected components of each dataset
profile_directed_hp_er.py   // bench on directed random generated network
profile_directed_hp_rw.py   // bench on directed random real-world network 
profile_directed_mp_rw.py		//  bench on directed real-world network in the multi-process case
profile_directed_mp_er.py 	//  bench on directed random generated network in the multi-process case
profile_undirected_hp_er.py  //  bench on undirected random generated network
profile_undirected_hp_rw.py	 //  bench on undirected real-world network 
profile_undirected_mp_rw.py  //  bench on undirected real-world network in the multi-process case

```

1. Open your terminal, make sure you have entered into right python environment that equipped with easygraph and igraph. 
2. Choose a script and run the script as follows：

```
python profile_directed_hp_rw.py
```







## Result visualization 




## Datasets


The `er_*` Erdos-Renyi random graphs are generated with `eg.erdos_renyi_M()`.

<!-- BEGIN DATASET TABLE -->

| Dataset Name                                                 | nodes   | edges   | is_directed | average_degree | density  |
| ------------------------------------------------------------ | ------- | ------- | ----------- | -------------- | -------- |
| ER\_10k\_u                                                   | 10,000  | 20,000  | False       | 4.0            | 5.0e-05  |
| ER\_50k\_u                                                   | 50,0000 | 100,000 | False       | 4.0            | 1.0e-05  |
| ER_100k_u                                                    | 100,000 | 200,000 | False       | 4.0            | 5.0e-06  |
| ER_200k_u                                                    | 200,000 | 400,000 | False       | 4.0            | 2.5e-06  |
| ER_10k_d                                                     | 10,000  | 20,000  | True        | 4.0            | 2.5e-05  |
| ER_50k_d                                                     | 50,000  | 10,000  | True        | 4.0            | 5.0e-06  |
| ER_100k_d                                                    | 100,000 | 200,000 | True        | 4.0            | 2.5e-06  |
| ER_200k_d                                                    | 200,000 | 400,000 | True        | 4.0            | 1.25e-06 |
| [ca-HepTh](http://snap.stanford.edu/data/ca-HepTh.html)      | 9877    | 25998   | False       | 5.26           | 0.0005   |
| [email-Enron](http://snap.stanford.edu/data/email-Enron.html) | 36692   | 183831  | False       | 10.02          | 0.0003   |
| [ca-HepPh](http://snap.stanford.edu/data/ca-HepPh.html)      | 12008   | 118521  | False       | 19.74          | 0.0016   |
| [ca-CondMat](http://snap.stanford.edu/data/ca-CondMat.html)  | 23133   | 93497   | False       | 8.08           | 0.0003   |
| [amazon0302](http://snap.stanford.edu/data/amazon0302.html)  | 262111  | 1234877 | True        | 9.42           | 1.79e-05 |
| [soc-Epinions1](http://snap.stanford.edu/data/soc-Epinions1.html) | 75879   | 508837  | True        | 13.41          | 8.8e−05  |
| [wikivote](http://snap.stanford.edu/data/wiki-Vote.html)     | 7115    | 103689  | True        | 29.15          | 0.0020   |
| pgp.edgelist                                                 | 39796   | 301498  | True        | 15.15          | 0.0002   |
| [p2p-Gnutella04](http://snap.stanford.edu/data/p2p-Gnutella04.html) | 10876   | 39994   | True        | 7.35           | 0.0003   |
| [soc-Slashdot0811](http://snap.stanford.edu/data/soc-Slashdot0811.html) | 77360   | 905468  | True        | 23.41          | 0.0002   |
| [web-NotreDame](http://snap.stanford.edu/data/web-NotreDame.html) | 325729  | 1497134 | True        | 9.19           | 1.5e−07  |
| [email-EuAll](http://snap.stanford.edu/data/email-Enron.html) | 265214  | 420045  | True        | 3.17           | 0.0003   |

