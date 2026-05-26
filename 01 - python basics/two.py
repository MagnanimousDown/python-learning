# Exercise 1
name = "Omkar"
age = 23
is_backend_dev = True

print(f"Hello, my name is {name} and I am {age} years old.")

# Exercise 2
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(f"Number: {n}")

# Exercise 3
def multiply (a: int, b: int) -> int:
    return a*b

product = multiply(3, 4)
print(f"The product of 3 and 4 is {product}")

# Exercise 4
class Car:
    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year
    
    def get_details(self):
        print(f"{self.brand} - {self.year}")

c1 = Car('Toyota', 2020)
c1.get_details()

user = {
    "name": "Aditya",
    "skills": ["NodeJS", "Express", "Prisma"]
}

for i in user["skills"]:
    print(i)