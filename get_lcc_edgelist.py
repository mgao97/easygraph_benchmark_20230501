#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2023-03-24
Purpose: Why not?
"""

import argparse
from pathlib import Path
import networkx as nx
# from config import edgelist_filenames

def load_un_graph(filename):
    return nx.read_edgelist(filename, delimiter="\t", nodetype=int, create_using=nx.Graph)

def load_graph(filename: str) -> nx.Graph:
    return nx.read_edgelist(filename, delimiter="\t", nodetype=int, create_using=nx.DiGraph)


def get_un_lcc(g: nx.Graph) -> nx.Graph:
    return nx.subgraph(g, max(nx.connected_components(g), key=len))

def get_lcc(g: nx.Graph) -> nx.Graph:
    return nx.subgraph(g, max(nx.strongly_connected_components(g), key=len))

def write_graph(g: nx.Graph, path: str):
    nx.write_edgelist(g, path, delimiter="\t", data=False)



def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Why not?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)




    return parser.parse_args()


def main():
    """Make a jazz noise here"""
    edgelist_filenames = [
         "/users/gtc/eg/easygraph-bench/directed_dataset/amazon0302.txt",
                "/users/gtc/eg/easygraph-bench/directed_dataset/pgp.edgelist",
                "/users/gtc/eg/easygraph-bench/directed_dataset/soc-Epinions1.txt",
                "/users/gtc/eg/easygraph-bench/directed_dataset/wiki-Vote.txt",
              "/users/gtc/eg/easygraph-bench/directed_dataset/p2p-Gnutella04.txt",
                "/users/gtc/eg/easygraph-bench/directed_dataset/web-NotreDame.txt",
                "/users/gtc/eg/easygraph-bench/directed_dataset/email-EuAll.txt",
                "/users/gtc/eg/easygraph-bench/directed_dataset/soc-Slashdot0811.txt",
                "/users/gtc/eg/easygraph-bench/directed_dataset/amazon0601.txt",
                "/users/gtc/eg/easygraph-bench/directed_dataset/soc-pokec-relationships.txt",
    ]
    
    un_edgelist_filenames=["/users/gtc/eg/easygraph-bench/undirected_datasets/ca-HepTh.txt",
                "/users/gtc/eg/easygraph-bench/undirected_datasets/email-Enron.txt",
                "/users/gtc/eg/easygraph-bench/undirected_datasets/lastfm_asia_edges.txt",
                "/users/gtc/eg/easygraph-bench/undirected_datasets/ca-HepPh.txt",
                "/users/gtc/eg/easygraph-bench/undirected_datasets/ca-CondMat.txt",]
    args = get_args()
    for filename in un_edgelist_filenames:
        new_path = Path(filename).with_stem(f"{Path(filename).stem}_lcc")
        if new_path.exists():
            continue
        # g = load_graph(filename)
        g = load_un_graph(filename)
        # lcc = get_lcc(g)
        lcc = get_un_lcc(g)
        write_graph(lcc, str(new_path))
        print(f'Converted {filename} to {new_path}')


if __name__ == '__main__':
    main()
