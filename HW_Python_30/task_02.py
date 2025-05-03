# Создайте класс BankAccount для представления банковского счета. Класс должен иметь
# атрибуты account_number (номер счета) и balance (баланс), а также методы deposit() для
# внесения денег на счет и withdraw() для снятия денег со счета. Затем создайте экземпляр
# класса BankAccount, внесите на счет некоторую сумму и снимите часть денег. Выведите
# оставшийся баланс. Не забудьте предусмотреть вариант, при котором при снятии баланс
# может стать меньше нуля. В этом случае уходить в минус не будем, вместо чего будем
# возвращать сообщение "Недостаточно средств на счете".
import decimal


class BankAccount:
    def __init__(self, account_number: int, balance=0):
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f"Счет '{self.account_number}'. Текущий баланс:'{self.balance}'"

    def deposit(self,dep):
        self.balance += dep
        print(f"Баланс счета {self.account_number} увеличен на {dep}. Текущий баланс: {self.balance}")

    def withdraw(self,draw):
        if self.balance < draw:
            print(f"Недостаточно средств на счете. Текущий баланс: {self.balance}")
        else:
            self.balance -= draw
            print(f"Баланс счета {self.account_number} уменьшен на {draw}. Текущий баланс: {self.balance}")

if __name__ == "__main__":
    new_account = BankAccount(123)
    print(new_account)
    new_account.deposit(10)
    new_account.withdraw(5.55)
    new_account.withdraw(12)

