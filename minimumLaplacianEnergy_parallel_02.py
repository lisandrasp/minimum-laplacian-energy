#!/usr/bin/env sage -python

# Second attempt at using the parallel decorator, doesn't work too
# SageMath parallelizes kirchhoff_matrix() without any issues but doesn't seem able to parallelize eigenvalues()
# eigenvalues() output is 'INVALID DATA Ran out of input'

from sage.all import *
import time

start = time.time()

n = 5
parameters = str(n) + " -c " + str(n) + ":" + str(n)
graphs_nauty = list(graphs.nauty_geng(parameters))


@parallel(ncpus=7)
def laplacian_energy(graphs):
    matrices = graphs.kirchhoff_matrix()
    eigen = matrices.eigenvalues()
    return eigen


spectrum_all = laplacian_energy(graphs_nauty)

for spectrum in spectrum_all:
    print(spectrum)

finish = time.time()
print(f'Execution time {round(finish - start, 2)} s')
