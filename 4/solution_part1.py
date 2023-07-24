num_fully_contained = 0

input = open("input", "r")

for line in input:
    [x,y] = line.strip().split(",")
    
    [lower_x, upper_x] = map(int, x.split("-"))
    [lower_y, upper_y] = map(int, y.split("-"))

    y_contains_x = upper_x <= upper_y and lower_x >= lower_y
    x_contains_y = upper_y <= upper_x and lower_y >= lower_x
    
    if x_contains_y or y_contains_x:
        num_fully_contained += 1

print(num_fully_contained)
