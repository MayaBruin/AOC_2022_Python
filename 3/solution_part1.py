sum_of_priorities = 0

def letter_to_priority(letter):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96

input = open("input", "r")

for line in input:
    halfway = len(line) // 2
    for char in line[:halfway]:
        if char in line[halfway:]:
            duplicate = char

    sum_of_priorities += letter_to_priority(duplicate)

print(sum_of_priorities)
