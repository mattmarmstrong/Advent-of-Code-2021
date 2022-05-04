input = open("2.txt", "r")

horizontal = 0
vertical = 0

for line in input:
    direction, distance = line.split(" ")
    distance = int(distance)

    print(direction, distance)
    print(horizontal, vertical)
    if direction == "forward":
        horizontal += distance
    elif direction == "up":
        vertical -= distance
    else:
        vertical += distance
    print(horizontal, vertical)

print(horizontal * vertical)