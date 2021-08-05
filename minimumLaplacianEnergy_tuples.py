#!/usr/bin/env sage -python

from sage.all import *

import time
import os

start = time.time()

n, m = 12, 12
parameters = str(n) + " -c " + str(m) + ":" + str(m)
graphs_nauty = list(graphs.nauty_geng(parameters))
print(f'Nauty list size {len(graphs_nauty)} Cycles {len(graphs_nauty) // 240}')

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

while f - 240 <= len(tuple_nauty) + 1:
    for graph_tuple in tuple_nauty[s:f]:
        new_energy = laplacian_energy(graph_tuple[1].spectrum(laplacian=True), n, m)
        new_index = graph_tuple[0]
        if new_energy < energy:
            energy = new_energy
            index = new_index
            graphs_nauty[index].plot().save(str('graph_partial_' + str(n) + '.png'))
            with open('energy.txt', 'w') as graph_info:
                graph_info.write(str(round(energy, 5)))
    s += 240
    f += 240
    cycle += 1
    print(f'Cycle {cycle} Partial minimum Laplacian energy {round(energy, 5)} Graph {index}')

finish = time.time()

graphs_nauty[index].plot().save(str('graph_' + str(n) + '.png'))

if os.path.exists(str('graph_' + str(n) + '.png')):
    os.remove(str('graph_partial_' + str(n) + '.png'))

print(f'Minimum Laplacian energy {round(energy, 5)}')
print(f'Execution time {round(finish - start, 2)} s')
