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
    for mu in spectrum:
        sum += abs(mu - 2 * m / n)
    return sum

def sigma(graph_tuple, spectrum):
    ''' Returns Sigma (number of laplacian eigenvalues greater or equal to the average degree). '''
    degree = graph_tuple.average_degree()
    return len([mi for mi in spectrum if mi >= degree])

def diameter(graph_tuple):
    ''' Returns the diameter of the graph (length of the "longest shortest path" between any two vertices). '''
    distance_all = graph_tuple.distance_all_pairs()
    distance_set = set()
    for dictionary in distance_all:
        for distance in distance_all[dictionary].values():
            distance_set.add(distance)
    return max(distance_set)

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
            graph_tuple = new_graph_tuple[1]
            index = new_index

            graphs_nauty[index].plot().save(str('graph_partial_' + str(n) + '.png'))

            with open('energy.txt', 'w') as graph_info:
                graph_info.write(str(round(energy, 5)))
    s += 240
    f += 240
    cycle += 1
    print(f'Cycle {cycle} Partial minimum Laplacian energy {round(energy, 5)} Graph {index}')


finish = time.time()

filename = 'graph_' + str(n) + '.png'
graphs_nauty[index].plot().save(filename)

if os.path.exists(str('graph_' + str(n) + '.png')):
    os.remove(str('graph_partial_' + str(n) + '.png'))

print(f'Minimum Laplacian energy {round(energy, 5)}')
print(f'Sigma {sigma(graph_tuple, spectrum)}')
print(f'Diameter {diameter(graph_tuple)}')
print(f'Execution time {round(finish - start, 2)} s')
