#!/usr/bin/env sage -python

from sage.all import *

n, m = 20, 20
c = 4


def laplacian_energy(spectrum, n, m):
    sum = 0
    for mi in spectrum:
        sum += abs(mi - 2 * m / n)
    return sum


tadpole = graphs.TadpoleGraph(c, n - c)
tadpole.plot().save('tadpole_' + str(n) + '.png')
print(f'Tadpole Laplacian energy {round(laplacian_energy(tadpole.spectrum(laplacian=True), n, m), 5)}')

cycle = graphs.CycleGraph(n)
cycle.plot().save('cycle_' + str(n) + '.png')
print(f'Cycle Laplacian energy {round(laplacian_energy(cycle.spectrum(laplacian=True), n, m), 5)}')
