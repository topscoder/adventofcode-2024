
import re

# input_file = "./task1-example.txt"
input_file = "./task1.txt"

left = []
right = []

with open(input_file, 'r') as file:
    for line in file:
        # print (line.strip())
        ids = re.findall("\d+", line.strip())
        left.append(ids[0])
        right.append(ids[1])


left.sort()
right.sort()


# print('left: ', left)
# print('right: ', right)

total_distance = 0

for i in range(len(left)):
    diff = abs(int(left[i])-int(right[i]))
    # print(left[i], " - ", right[i], " = ", diff)
    total_distance += diff

print("The total distance between the lists is: ", total_distance)