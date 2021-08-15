#!/usr/bin/env sage -python

from sage.all import *
import time

start = time.time()

n, m = 12, 12
parameters = str(n) + " -c " + str(m) + ":" + str(m)
graphs_nauty = list(graphs.nauty_geng(parameters))


def laplacian_energy(spectrum, n, m):
    sum = 0
    for mu in spectrum:
        sum += abs(mu - 2 * m / n)
    return sum


matrices = [graph.kirchhoff_matrix(signless=True) for graph in graphs_nauty]
energy = [laplacian_energy(matrix.eigenvalues(), n, m) for matrix in matrices]

finish = time.time()

index = energy.index(min(energy))
filename = 'graph_' + str(n) + '.png'
graphs_nauty[index].plot().save(filename)
print('Minimum signless Laplacian energy', round(min(energy), 5))
print(f'Execution time {round(finish - start, 2)} s')
