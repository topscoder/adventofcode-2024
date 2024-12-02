
import re

# input_file = "./task1-example.txt"
input_file = "./task1.txt"

left = []
right = []

with open(input_file, 'r') as file:
    for line in file:
        # print (line.strip())
        ids = re.findall(r"\d+", line.strip())
        left.append(ids[0])
        right.append(ids[1])


# print('left: ', left)
# print('right: ', right)

similarity = 0

for i in range(len(left)):
    # print(left[i], " - ", right[i], " = ", diff)

    occurrence = right.count(left[i])
    # print(left[i], " occurs ", occurrence, " times")

    similarity += (int(left[i]) * int(occurrence))


print("The similarity score is: ", similarity)