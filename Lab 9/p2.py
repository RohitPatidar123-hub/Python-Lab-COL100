# pattern = input()
# path = input()

# f = open(path)  ##f is file object that is iterate line by line
# s=f.readline()
# print("f.readline() only one line : ",s)

# s=f.readlines()
# print("f.readlines() read complete line : ",s)
# for l in f:
#     #if pattern in l:
#         r=int(l.strip())
#         print(r)
#         print(type(r))
import os

def sum_integers_in_files(path):
    total_sum = 0
    if os.path.isdir(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            total_sum += sum_integers_in_files(item_path)

    elif path.endswith(".txt"):
        with open(path, 'r') as file:
            for line in file:
                total_sum += int(line.strip())
    return total_sum

base_dir = input("Enter the path to the Data directory: ")

with open("p2_output.txt", "w") as output_file:
    for i in range(1, 11):
        dir_name = f"D{i}"
        dir_path = os.path.join(base_dir, dir_name)
        if os.path.isdir(dir_path):
            dir_sum = sum_integers_in_files(dir_path)
            #output_file.write(f"{dir_sum}\n")
            print(dir_sum)