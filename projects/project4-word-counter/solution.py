# Project 4 — Word Counter
# Author: Şevval Özlü

sentence = input("Enter a sentence: ")
#BONUS: remove punctuation
sentence = sentence.replace(",", "").replace("!", "").replace("?", "")

words = sentence.lower().split()

# TODO: total word count using len()
total_words =len(words)

# TODO: character count (no spaces)
total_characters = len(sentence.replace(" ", ""))
# Hint: sentence.replace(" ", "") removes all spaces, then use len()

# TODO: word frequency dictionary
frequency = {}
for word in words:
    if word in frequency:
      frequency[word] += 1
    else:
      frequency[word] = 1
#BONUS: sort from most to least common
sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

# TODO: print total words, total characters, then word frequency
print(f"Total words: {total_words}")
print(f"Total characters (no spaces): {total_characters}")
print("Word frequency:")

for word, count in sorted_words:
  print(f"{word} -> {count}")
