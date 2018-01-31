from threading import Thread as Task
from time import sleep

class BankAccount(object):
    def __init__(self, owner, initial_deposit):
        self.amount = initial_deposit
        self.owner = owner

    def __str__(self):
        return "%s: %s€" % (self.owner, self.amount)

    def virement(self, money):
        self.amount += money

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

