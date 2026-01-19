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
