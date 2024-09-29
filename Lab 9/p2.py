pattern = input()
path = input()

f = open(path)  ##f is file object that is iterate line by line
s=f.readline()
print("f.readline() only one line : ",s)

s=f.readlines()
print("f.readlines() read complete line : ",s)
for l in f:
    #if pattern in l:
        r=int(l.strip())
        print(r)
        print(type(r))