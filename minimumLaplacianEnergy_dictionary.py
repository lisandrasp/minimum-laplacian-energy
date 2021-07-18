#!/usr/bin/env sage -python

# A bit slower than minimumLaplacianEnergy_tuples

from sage.all import *

import time

start = time.time()

n, m = 10, 10
parameters = str(n) + " -c " + str(m) + ":" + str(m)
graphs_nauty = list(graphs.nauty_geng(parameters))
print('Nauty list size', len(graphs_nauty))

nauty_dict = dict()
for index, graph in enumerate(graphs_nauty):
    nauty_dict[index] = graph


def laplacian_energy(spectrum, n, m):
    sum = 0
    for mi in spectrum:
        sum += abs(mi - 2 * m / n)
    return sum


energy = laplacian_energy(graphs_nauty[0].spectrum(laplacian=True), n, m)
index = 0

for idx, graph in nauty_dict.items():
    new_energy = laplacian_energy(graph.spectrum(laplacian=True), n, m)
    new_idx = idx
    if new_energy < energy:
        energy = new_energy
        index = new_idx
        print(f'Partial minimum Laplacian energy {round(energy, 5)} Graph {index}')

finish = time.time()

filename = 'graph_' + str(n) + '.png'
graphs_nauty[index].plot().save(filename)
print('Minimum Laplacian energy', round(energy, 5))
print(f'Execution time {round(finish - start, 2)} s')
