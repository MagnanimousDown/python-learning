name = 'xyz'
age = 23

print("Hello")
print("hello", name)

message = f"Hello {name}"

print(message)

num = [1,2,3]

print(num[0])

user = {
    "name": "Omkar",
    "age": 23
}

print(user["name"])

if user["age"] > 18:
    print("Adult")

for n in num:
    print(n)

def add(a, b):
    return a + b

sum = add(1, 3)

print(f"Sum is {sum}")