#!/usr/bin/env sage -python

# Works the same as minimumLaplacianEnergy.py but picks the first and second minimum values

from sage.all import *
import time

start = time.time()

n, m = 10, 10
parameters = str(n) + " -c " + str(m) + ":" + str(m)

graphs_nauty = list(graphs.nauty_geng(parameters))


def laplacian_energy(spectrum, n, m):
    sum = 0
    for mi in spectrum:
        sum += abs(mi - 2 * m / n)
    return sum


energy = [laplacian_energy(graph.spectrum(laplacian=True), n, m) for graph in graphs_nauty]

finish = time.time()

index = energy.index(min(energy))
filename1 = 'graph_01_' + str(n) + '.png'
graphs_nauty[index].plot().save(filename1)
print(f'Minimum Laplacian energy {round(min(energy), 5)}')

del energy[index]

new_index = energy.index(min(energy))
filename2 = 'graph_02_' + str(n) + '.png'
graphs_nauty[new_index].plot().save(filename2)
print(f'Second minimum Laplacian energy {round(min(energy), 5)}', '\n')
print(f'Execution time {round(finish - start, 2)} s')
