import threading
import random
from time import sleep
lock = threading.Lock()

class Bank:
    balance = 0


    def deposit(self):
        transactions = 5
        lock.acquire()
        for i in range(transactions+1):
            random_int = round(random.uniform(50, 500))
            for r in range(1):
                self.balance += random_int
                if self.balance >= 500 and lock == lock.locked():
                    lock.release()
                print("Пополнение", random_int,". Баланс: ",self.balance)
                sleep(0.001)

    def take(self):
        withdrawal = 5
        for t in range(withdrawal+1):
            random_numb = round(random.uniform(50, 500))
            for e in range(1):
                print("Запрос на ", random_numb)
                if random_numb <= self.balance:
                    self.balance = self.balance - random_numb
                    print("Снятие: ", random_numb,". Баланс: ",self.balance)

                if random_numb > self.balance:
                    print("Запрос отклонён, недостаточно средств")
        lock.acquire()


gera = Bank()
rtr = threading.Thread(gera.deposit())
eee = threading.Thread(gera.take())
rtr.start()
eee.start()
