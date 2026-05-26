# Exercise 1 — List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [number * number for number in numbers]

print(squares)

# Exercise 2 — Filter evens
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Exercise 3 — enumerate
fruits = ["apple", "banana", "mango"]
for index, value in enumerate(fruits):
    print(index, value)

# Exercise 4 — Safe dictionary access
user = {
    "name": "Omkar"
}

print(user.get("name"))
print(user.get("email"))

# Exercise 5 — Dataclass
from dataclasses import dataclass

@dataclass
class User():
    name: str
    age: int

    # def print_name(self):
    #     print(f"{self.name} and {self.age}")

u1 = User("Omkar", 23)
# u1.print_name()
print(u1)

# Bonus challenge
users = [
    {"name": "Om", "age": 23},
    {"name": "Rahul", "age": 17},
    {"name": "Amit", "age": 30}
]

adult = [user["name"] for user in users if user["age"] >= 18]
print(adult)