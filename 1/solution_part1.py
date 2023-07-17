input = open("input", "r")

this_elf_cal = 0
maxcal = 0
elf_with_maxcal = 1
current_elf = 1

def nextelf():
    global maxcal
    global current_elf
    global elf_with_maxcal
    global this_elf_cal

    if this_elf_cal > maxcal:
        maxcal = this_elf_cal
        elf_with_maxcal = current_elf
        
    current_elf += 1
    this_elf_cal = 0

for line in input:
    if line == "\n":
        nextelf()
        continue
    
    this_elf_cal += int(line)

print("maxcal is " + str(maxcal) + " on elf number " + str(elf_with_maxcal))
