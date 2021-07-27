#!/usr/bin/env sage -python

from sage.all import *

n, m = 20, 20


def laplacian_energy(spectrum, n, m):
    sum = 0
    for mi in spectrum:
        sum += abs(mi - 2 * m / n)
    return sum


cycle = graphs.CycleGraph(4)
path = graphs.PathGraph(n - 4 + 1)
tadpole = cycle.disjoint_union(path)
tadpole.merge_vertices([(0, 0), (1, 0)])
tadpole.plot().save('tadpole_' + str(n) + '.png')
print(f'Tadpole Laplacian energy {round(laplacian_energy(tadpole.spectrum(laplacian=True), n, m), 5)}')

cycle_graph = graphs.CycleGraph(n)
cycle_graph.plot().save('cycle_' + str(n) + '.png')
print(f'Cycle Laplacian energy {round(laplacian_energy(cycle_graph.spectrum(laplacian=True), n, m), 5)}')
