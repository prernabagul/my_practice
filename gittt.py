# list_comprehension.py

numbers = [1, 2, 3, 4, 5, 6]

squares = [n**2 for n in numbers]
evens = [n for n in numbers if n % 2 == 0]

print("Squares:", squares)
print("Evens:", evens)
cubes = [n**3 for n in numbers]
print("Cubes:", cubes)
