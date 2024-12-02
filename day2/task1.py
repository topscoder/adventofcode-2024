import re

# input_file = "./task1-example.txt"
input_file = "./task1.txt"

safe = 0


def safe_increments(levels):
    for i in range(len(levels)-1):
        if abs(levels[i] - levels[i+1]) == 0:
            print(levels, ": Unsafe, Neither an increase or a decrease")
            return False # Neither an increase or a decrease
        
        elif abs(levels[i] - levels[i+1]) > 3:
            print(levels, ": Unsafe, increase or decrease > 3")
            return False # Increase > 3 not safe
        
    return True


def is_incrementing(levels):
    return sorted(levels) == levels


def is_decrementing(levels):
    return sorted(levels, reverse = True) == levels


with open(input_file, 'r') as file:
    for line in file:
        report = line.strip()
        levels = report.split(" ")

        for i in range(len(levels)):
            levels[i] = int(levels[i])

        # report is safe when:
        # (1) The levels are either all increasing or all decreasing.
        # (2) Any two adjacent levels differ by at least one and at most three.
        if (is_incrementing(levels) or is_decrementing(levels)) and safe_increments(levels) is True:
            print(levels, ": Safe, levels are increasing or decreasing with => 1 and <= 3")
            safe += 1


print("The amount of safe reports: ", safe)