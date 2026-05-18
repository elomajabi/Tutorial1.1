# Ask the user for a sentence.
#
# Count how many times each word appears.
#
# Example:
# Input:
# cat dog cat bird dog cat
#
# Output:
# cat -> 3
# dog -> 2
# bird -> 1

sentence = input("Your sentence: ")
words = sentence.lower().split()
count = {}

for word in words:
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1

for word in count:
    print(word, "->", count[word])