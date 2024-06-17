import sys

args = sys.argv[1:]
num = 0
for i in args:
    num += int(i)

print(num)