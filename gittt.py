# list_comprehension.py

numbers = [1, 2, 3, 4, 5, 6]

squares = [n**2 for n in numbers]
evens = [n for n in numbers if n % 2 == 0]

print("Squares:", squares)
print("Evens:", evens)
cubes = [n**3 for n in numbers]
print("Cubes:", cubes)
odds = [n for n in numbers if n % 2 != 0]
print("Odds:", odds)

# logging_demo.py

import logging

logging.basicConfig(level=logging.INFO)

logging.info("Application started")
logging.warning("Low memory warning")
logging.error("Error occurred")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Application finished")
logging.shutdown()
