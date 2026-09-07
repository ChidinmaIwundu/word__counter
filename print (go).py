text = input("Put in a sentence: ")
print(len(text))

word_count = len(text.split())
print(word_count)

target_letter = input("Which letter do you want to count? ")
letter_count = 0

for char in text:
    if char == target_letter:
        letter_count = letter_count + 1

print(letter_count)