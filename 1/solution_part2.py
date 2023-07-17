input = open("input", "r")

this_elf_cal = 0
current_elf = 1

three_largest = [0, 0, 0]

def nextelf():
    global current_elf
    global this_elf_cal
    global three_largest

    if this_elf_cal > three_largest[0]:
        three_largest[0] = this_elf_cal
        three_largest.sort()
        
    current_elf += 1
    this_elf_cal = 0

for line in input:
    if line == "\n":
        nextelf()
        continue
    
    this_elf_cal += int(line)

print("The sum of the three largest elfs calories is " + str(sum(three_largest)))
