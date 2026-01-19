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
