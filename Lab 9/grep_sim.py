pattern = input()
path = input()

f = open(path)  ##f is file object that is iterate line by line
for l in f:
    if pattern in l:
        print(l.strip())

