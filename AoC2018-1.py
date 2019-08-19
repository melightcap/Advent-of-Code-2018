#Day 1: Chronal Calibration
file = open("input1.txt","r")
content = file.readlines()
file.close()

frequency = 0

content = list(map(int,content))

for item in content:
    frequency += item

print(frequency)
