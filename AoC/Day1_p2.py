input = open("1.txt", "r")

data = list(map(int, input.readlines()))

incr = 0


for i in range(len(data) - 3):
    if (data[i] + data[i+1] + data[i+2]) < (data[i+1] + data[i+2] + data[i+3]):
        incr += 1

print("Number of measurements larger than previous measurement in sliding window: " + str(incr))
