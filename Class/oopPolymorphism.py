class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

#same method call-different results, this is polymorphism in action
shapes = [Rectangle(2, 3), Circle(3)]
for shape in shapes:
    print(shape.area())
""""------------------------------------------------------------------------------------------------"""
#Abstraction
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(PaymentGateway):
        def pay(self, amount):
            return f"Paid ${amount} using Card"
        
class TransferPayment(PaymentGateway):
        def pay(self, amount):
            return f"Paid ${amount} using Bank Transfer"

card= CardPayment()
transfer= TransferPayment()
print(card.pay(100))
print(transfer.pay(200))