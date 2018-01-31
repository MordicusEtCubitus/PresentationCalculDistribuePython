from multiprocessing import Process as Task, Lock
from time import sleep

class BankAccount(object):
    def __init__(self, owner, initial_deposit):
        self.amount = initial_deposit
        self.owner = owner
        self.lock = Lock()

    def __str__(self):
        return "%s: %s€" % (self.owner, self.amount)

    def virement(self, money):

        with self.lock:
            # get current amount
            current_amount = self.amount

            # network slow time
            sleep(0.01)

            # doing computation
            current_amount += money

            # hard drive latency
            sleep(0.01)

            self.amount = current_amount

my_account = BankAccount("Me", 1.0)
print("Start:", my_account)

tasks = []
for ind in range(0, 100):
    t = Task(target=my_account.virement, args=(100,))
    t.start()
    tasks.append(t)

print('Waiting end of tasks')
[ t.join() for t in tasks]
print("End:", my_account)

