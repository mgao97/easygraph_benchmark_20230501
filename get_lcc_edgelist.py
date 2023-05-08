#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2023-03-24
Purpose: Why not?
"""

import argparse
from pathlib import Path
import networkx as nx
import numpy as np
import os

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


def pre_data(path, file):
    # print(file)
    data = np.loadtxt(path+file,usecols=(0,1))
    np.savetxt(path+file, data, fmt='%i')
    return path+file

def main():
    u_filepath = 'datasets/undirected_datasets/'
    u_filelist = os.listdir(u_filepath)
    print(u_filelist)

    d_filepath = 'datasets/directed_datasets/'
    d_filelist = os.listdir(d_filepath)
    print(d_filelist)
    
    print('get lcc of undirected network datasets..............')
    for file in u_filepath:
        new_path = Path(file).with_stem(f"{Path(file).stem}_lcc")
        if new_path.exists():
            continue
        g = load_un_graph(file)
        
        lcc = get_un_lcc(g)
        write_graph(lcc, str(new_path))
        print(f'Converted {file} to {new_path}')

    print('get lcc of directed network datasets..............')
    for file in d_filepath:
        new_path = Path(file).with_stem(f"{Path(file).stem}_lcc")
        if new_path.exists():
            continue
        g = load_un_graph(file)
        
        lcc = get_lcc(g)
        write_graph(lcc, str(new_path))
        print(f'Converted {file} to {new_path}')


if __name__ == '__main__':
    main()
