#!/usr/bin/env sage -python

# First attempt at using the parallel decorator, doesn't work
# eigenvalues() output is 'NO DATA'

from sage.all import *
import time

start = time.time()

n = 4
parameters = str(n) + " -c " + str(n) + ":" + str(n)
graphs_nauty = list(graphs.nauty_geng(parameters))


def matrices(graph_in):
    return [graph.kirchhoff_matrix() for graph in graph_in]


@parallel(ncpus=7)
def eigen(matrix_in):
    return [matrix.eigenvalues() for matrix in matrix_in]


matrices_all = matrices(graphs_nauty)
spectrum_all = eigen(matrices_all)

for spectrum in spectrum_all:
    print(spectrum)

finish = time.time()
print(f'Execution time {round(finish - start, 5)} s')
