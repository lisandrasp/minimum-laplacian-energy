#!/usr/bin/env sage -python

# Slightly faster than minimumLaplacianEnergy.py and less likely to run out of RAM for bigger n, m

from sage.all import *
import time

start = time.time()

n, m = 5, 5
parameters = str(n) + " -c " + str(m) + ":" + str(m)
graphs_nauty = list(graphs.nauty_geng(parameters))


def laplacian_energy(spectrum, n, m):
    sum = 0
    for mi in spectrum:
        sum += abs(mi - 2 * m / n)
    return sum


size = 240
graphs_list = [graphs_nauty[i:i + n] for i in range(0, len(graphs_nauty), size)]

spectrum_all = list()

for graph in graphs_list:
    spectrum_list = [list1.spectrum(laplacian=True) for list1 in graph]
    spectrum_all.append(spectrum_list)

spectrum_join = list()

for list2 in spectrum_all:
    spectrum_join += list2

energy = [laplacian_energy(list3, n, m) for list3 in spectrum_join]

finish = time.time()

index = energy.index(min(energy))
filename = 'graph_' + str(n) + '.png'
graphs_nauty[index].plot().save(filename)
print(f'Minimum Laplacian energy {round(min(energy), 5)}')
print(f'Execution time {round(finish - start, 2)} s')
