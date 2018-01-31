# coding=utf8
import sys
import numpy as np
import time

n = 100

times = []

while n <= 2000:
    mat = np.random.rand(n,n)
    
    # Compute dot product (do a lot of additions and multiplications)
    start = time.time()
    r = np.dot(mat, mat) # mat @ mat
    end = time.time()
    
    compute_time = end - start
    times.append((n, compute_time))
    print(n, compute_time)
    n += 200
    
# Save it to a file
np.save(sys.argv[1], times)