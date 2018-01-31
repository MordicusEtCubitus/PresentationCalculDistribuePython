from celery import Celery


my_app = Celery(
    "My worker",
    broker='amqp://guest:guest@localhost/'
    # broker="amqp://celery:celery@192.168.1.5/celery_vhost"
)

# On indique que la fonction est parallélisable sur
# les workers/pool de process Celery
@my_app.task
def cube(x):
    print("Compute %s**3" % x)
    return x**3


# Lancer ce script avec la commande shell
# depuis le dossier parent du dossier qui contient ce script
# ici le parent de parallel
# celery worker -A application.my_app --loglevel=info
