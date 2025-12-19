# from abc import ABC, abstractmethod


# class Payment(ABC):
#     def __init__(self, amount):
#         self.__amount = amount   

#     def get_amount(self):
#         return self.__amount

#     @abstractmethod
#     def pay(self):
#         pass


# class CardPayment(Payment):
#     def pay(self):
#         print(f"Paid ₹{self.get_amount()} using Card")

# class UPIPayment(Payment):
#     def pay(self):
#         print(f"Paid ₹{self.get_amount()} using UPI")

# class BankPayment(Payment):
#     def pay(self):
#         print(f"Paid ₹{self.get_amount()} using Bank Transfer")


# p1 = CardPayment(1000)
# p2 = UPIPayment(500)
# p3 = BankPayment(2000)

# for payment in (p1, p2, p3):
#     payment.pay()



# from abc import ABC, abstractmethod

# class Player(ABC):
#     def __init__(self, content):
#         self._content = content   

#     @abstractmethod
#     def play(self):
#         pass

# class TV(Player):
#     def play(self):
#         print(f"Playing '{self._content}' on TV")

# class Mobile(Player):
#     def play(self):
#         print(f"Playing '{self._content}' on Mobile")

# class Tablet(Player):
#     def play(self):
#         print(f"Playing '{self._content}' on Tablet")


# devices = [
#     TV("Movie"),
#     Mobile("Song"),
#     Tablet("Lecture")
# ]

# for device in devices:
#     device.play()


# from abc import ABC, abstractmethod

# class Notification(ABC):
#     def __init__(self, message):
#         self.__message = message  

#     def get_message(self):
#         return self.__message

#     @abstractmethod
#     def send(self):
#         pass

# class WhatsApp(Notification):
#     def send(self):
#         print(f"Sending WhatsApp message: {self.get_message()}")

# class Email(Notification):
#     def send(self):
#         print(f"Sending Email: {self.get_message()}")

# class SMS(Notification):
#     def send(self):
#         print(f"Sending SMS: {self.get_message()}")


# notifications = [
#     WhatsApp("Order Confirmed"),
#     Email("Welcome to our service"),
#     SMS("OTP is 1234")
# ]

# for n in notifications:
#     n.send()

# from abc import ABC, abstractmethod

# class ATM(ABC):
#     def __init__(self, balance):
#         self.__balance = balance  

#     def get_balance(self):
#         return self.__balance

#     def _update_balance(self, amount):
#         self.__balance += amount

#     @abstractmethod
#     def withdraw(self, amount):
#         pass

#     @abstractmethod
#     def deposit(self, amount):
#         pass

# class ATMService(ATM):
#     def withdraw(self, amount):
#         if amount <= self.get_balance():
#             self._update_balance(-amount)
#             print(f"Withdrawn ₹{amount}")
#         else:
#             print("Insufficient Balance")

#     def deposit(self, amount):
#         self._update_balance(amount)
#         print(f"Deposited ₹{amount}")

#     def check_balance(self):
#         print(f"Current Balance: ₹{self.get_balance()}")


# atm = ATMService(5000)
# atm.deposit(2000)
# atm.withdraw(3000)
# atm.check_balance()