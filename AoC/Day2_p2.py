input = open("2.txt", "r")

horizontal = 0
vertical = 0
aim = 0

for line in input:
    direction, distance = line.split(" ")
    distance = int(distance)

    print(direction, distance)
    print(horizontal, vertical)
    if direction == "forward":
        horizontal += distance
        vertical += aim * distance
    elif direction == "up":
        aim -= distance
    else:
        aim += distance
    print(horizontal, vertical, aim)

print(vertical * horizontal)