from multiprocessing import Pool

from time import sleep
import os
from functools import reduce

def carre(x):
    print("Calcul du carré de %s par proccesus %s" % (x, os.getpid()))
    sleep(1)
    return (x, x * x)


def init_process():
    print("Initializing process %s" %(os.getpid(),))

if __name__ == "__main__":

    pool = Pool(processes=3, initializer=init_process, initargs=(),
                maxtasksperchild=2)

    with pool:
        print("Running map")
        data = pool.map(carre, range(20))
        print("End map")
        print(data)