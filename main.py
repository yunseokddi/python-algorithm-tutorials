from dataclasses import dataclass

@dataclass
class Product:
    weight: int = None
    price: float = None

apple = Product()
apple.price = 10
apple.weight = 100
print(apple.price, apple.weight, sep=',')

