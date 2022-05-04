import sys

input = open("1.txt", "r")

data = list(map(int, input.readlines()))

incr = 0

for i in range(len(data) - 1):
    if data[i + 1] > data[i]:
        incr += 1

print("Number of measurements larger than previous measurement: " + str(incr))


