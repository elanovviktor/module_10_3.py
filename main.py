import time
import random
import threading
from threading import Thread, Lock
class Bank(Thread):
     def __init__(self):
         super().__init__()
         self.balance = 0
         self.lock = Lock()

     def deposit(self):
         for i in range(100):
             if self.balance >= 500 and self.lock.locked():
                 self.lock.release()
             random_int = random.randint(50, 500)
             self.balance += random_int
             print(f'Пополнение: {random_int}. Баланс: {self.balance}')
             time.sleep(0.001)
     def take(self):
         for i in range(100):
             random2_int = random.randint(50, 500)
             print(f'запрос на {random2_int}')
             if self.balance >= random2_int:
                 self.balance -= random2_int
                 print(f'снятие: {random2_int}. Баланс: {self.balance}')
             else:
                 print('запрос отклонен, недостаточно средств')
                 self.lock.ackuire()
             time.sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
