# text_analyzer.py

text = """Python is easy to learn.
Python is powerful.
Python is popular."""

words = text.lower().split()
word_count = {}

for word in words:
    word = word.strip(".")
    word_count[word] = word_count.get(word, 0) + 1

print("Word Frequency:")
for k, v in word_count.items():
    print(k, ":", v)


# email_validator.py

emails = [
    "user@gmail.com",
    "wrong-email",
    "admin@company.org"
]

for email in emails:
    if "@" in email and "." in email:
        print(email, "is valid")
    else:
        print(email, "is invalid")


# duplicate_finder.py

numbers = [1, 2, 3, 2, 4, 5, 1, 6]

duplicates = set()
seen = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    seen.add(num)

print("Duplicates:", duplicates)

# datetime_analyzer.py

from datetime import datetime

now = datetime.now()

print("Current Date:", now.date())
print("Current Time:", now.time())
print("Year:", now.year)

# prime_checker.py

numbers = [2, 3, 4, 5, 10, 11, 13]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in numbers:
    print(num, "Prime" if is_prime(num) else "Not Prime")

# write_file.py

lines = ["Python\n", "Data\n", "ML\n"]

with open("output.txt", "w") as file:
    file.writelines(lines)

print("File written successfully")
