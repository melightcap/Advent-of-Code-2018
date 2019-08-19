#Day 1: Chronal Calibration
file = open("input1.txt","r")
content = file.readlines()
file.close()

frequency = 0

repeat = set()
loop = True

content = list(map(int,content))

while loop:
    for item in content:
        frequency += item
        if frequency in repeat:
            loop = False
            break
        else:
            repeat.add(frequency)

print("First frequency reached twice is",frequency)
