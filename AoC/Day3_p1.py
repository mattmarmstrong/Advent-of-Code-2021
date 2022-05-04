input = open("3.txt", "r")

raw = list(map(str, input.readlines()))

data = [s.strip() for s in raw]


print(data)

gamma = ""
epsilon = ""

for i in range(len(data[0])):
    zeros = 0
    ones = 0

    for j in range(len(data)):
        if int(data[j][i]) == 0:
            zeros += 1
        else:
            ones += 1

    if ones >= zeros:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"


print(int(gamma, 2) * int(epsilon, 2))


