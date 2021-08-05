#!/usr/bin/env sage -python

from sage.all import *

import time
import os

start = time.time()

n, m = 10, 10
parameters = str(n) + " -c " + str(m) + ":" + str(m)
graphs_nauty = list(graphs.nauty_geng(parameters))
print(f'Nauty list size {len(graphs_nauty)} Cycles {len(graphs_nauty) // 240 + 1}')

list_nauty = list()

for index, graph in enumerate(graphs_nauty):
    list_nauty.append((index, graph))

tuple_nauty = tuple(list_nauty)


def laplacian_energy(spectrum, n, m):
    sum = 0
    for mi in spectrum:
        sum += abs(mi - 2 * m / n)
    return sum


energy = laplacian_energy(graphs_nauty[0].spectrum(laplacian=True), n, m)
index = 0
cycle = 0
s = 0
f = 240
spectrum = list()
graph_tuple = tuple()

while f - 240 <= len(tuple_nauty) + 1:
    for new_graph_tuple in tuple_nauty[s:f]:
        new_spectrum = new_graph_tuple[1].spectrum(laplacian=True)
        new_energy = laplacian_energy(new_spectrum, n, m)
        new_index = new_graph_tuple[0]

        if new_energy < energy:
            spectrum = new_spectrum
            energy = new_energy
            graph_tuple = new_graph_tuple
            index = new_index

            graphs_nauty[index].plot().save(str('graph_partial_' + str(n) + '.png'))

            with open('energy.txt', 'w') as graph_info:
                graph_info.write(str(round(energy, 5)))
    s += 240
    f += 240
    cycle += 1
    print(f'Cycle {cycle} Partial minimum Laplacian energy {round(energy, 5)} Graph {index}')

# Sigma is number of laplacian eigenvalues greater or equal to the average degree
degree = graph_tuple[1].average_degree()
sigma = len([mi for mi in spectrum if mi >= degree])

diameter = graph_tuple[1].diameter()

finish = time.time()

graphs_nauty[index].plot().save(str('graph_' + str(n) + '.png'))

if os.path.exists(str('graph_' + str(n) + '.png')):
    os.remove(str('graph_partial_' + str(n) + '.png'))

print(f'Minimum Laplacian energy {round(energy, 5)}')
print(f'Sigma {sigma}')
print(f'Diameter {diameter}')
print(f'Execution time {round(finish - start, 2)} s')
