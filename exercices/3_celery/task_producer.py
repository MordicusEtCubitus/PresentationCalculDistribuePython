from application import cube

for x in range(500):
    # cube(x) # exécute normalement la fonction
    cube.delay(x) # ajoute la tâche au serveur de tâches

