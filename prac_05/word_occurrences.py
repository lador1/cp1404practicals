"""
Word Occurrences
Estimate: 20 minutes
Actual:   28 minutes

"""

word_to_count = {}
text = input("Text: ")
words = text.split()
for word in sorted(words):
    word_frequency = word_to_count.get(word, 0) #.get returns keyname/value doesnt exist yet
    word_to_count[word] = word_frequency + 1

words = list(word_to_count.keys())
print(word_to_count)

max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")

