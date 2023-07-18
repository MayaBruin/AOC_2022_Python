sum_of_priorities = 0
elf_number_in_group = 1

group = ["", "", ""]

def letter_to_priority(letter):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96

input = open("input", "r")
list_of_lines = input.readlines()

for i in range(0, len(list_of_lines), 3):
    group = list_of_lines[i:i+3]
    
    for char in group[0]:
        if char != "\n" and char in group[1] and char in group[2]:
            badge = char

    sum_of_priorities += letter_to_priority(badge)

print(sum_of_priorities)
