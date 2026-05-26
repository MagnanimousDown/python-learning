from math_utils import add, subtract

result1 = add(3, 4)

result2 = subtract(3, 4)

print(f"{result1}, {result2}")

# Exercise 3 — Dataclass retry
from dataclasses import dataclass

@dataclass
class Product():
    name: str
    price: int

p1 = Product("Shampoo", 1000)

print(p1)

# Exercise 4 — Dictionary comprehension
numbers = [1, 2, 3, 4]

squares = {number: number * number for number in numbers}
print(squares)

