import timeit
from threading import Thread
from multiprocessing import Process

def countdown(n):
    while n > 0:
        n -= 1

def serial(n, repeat=2):
    for ind in range(repeat):
        countdown(n)


def threads(n, repeat=2):
    tasks = []
    for ind in range(repeat):
        t = Thread(target=countdown, args=(n,))
        t.start()
        tasks.append(t)

    [t.join() for t in tasks]

def processes(n, repeat=2):
    tasks = []
    for ind in range(repeat):
        t = Process(target=countdown, args=(n,))
        t.start()
        tasks.append(t)

    [t.join() for t in tasks]

print("Exécution en série")
N=10**8
repeat = 2
r = timeit.timeit(stmt="serial(N,repeat)"
                  , number=1
                  , globals=globals() # utilise les variables globales du script
                                      # permet de définir def countdown et def serial
                                      # pour le processus exécutant timeit
    )
print("serial:", r)

r = timeit.timeit(stmt="threads(N,repeat)"
                  , number=1
                  , globals=globals() # utilise les variables globales du script
                                      # permet de définir def countdown et def serial
                                      # pour le processus exécutant timeit
    )
print("threads:", r)

r = timeit.timeit(stmt="processes(N,repeat)"
                  , number=1
                  , globals=globals() # utilise les variables globales du script
                                      # permet de définir def countdown et def serial
                                      # pour le processus exécutant timeit
    )
print("processes:", r)

