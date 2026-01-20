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


