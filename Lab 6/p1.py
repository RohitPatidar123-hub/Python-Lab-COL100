def squares_till_n(n):
    result = []
    i=1
    while i*i<=n:
         result.append(i*i)
         i=i+1
    #Write your code here
    return result
    
   ############################ Do Not Change #################################

def solution(inp):
    return squares_till_n(*inp)

def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines]
    pos = 0
    num_tests = int(lines[0])
    input_tests = []
    for t in range(num_tests):
        pos += 1
        a = int(lines[pos])
        input_tests += [[a]]
    return input_tests

if __name__ == "__main__":
    Input = process_input(r'C:\Mtech\COL 100 Python\Python-Lab-COL100\Lab 6\p1_input.txt')
    for inp in Input:
        print(solution(inp))


