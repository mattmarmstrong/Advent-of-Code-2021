input = open("3.txt", "r")

raw = list(map(str, input.readlines()))

data = [s.strip() for s in raw]

csr = data

key = ""
for i in range(len(data[0])):
    zeros = 0
    ones = 0

    for j in range(len(data)):
        if int(data[j][i]) == 0:
            zeros += 1

        else:
            ones += 1

