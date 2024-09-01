def power_factorial(n, p):
    # Write your code here
    pow=1
    sum=0
    while n//p**pow:
        sum=sum+n//p**pow
        pow=pow+1
    return sum    


def solution(inp):
    return power_factorial(*inp)

def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines]
    pos = 0
    num_tests = int(lines[0])
    input_tests = []
    for t in range(num_tests):
        pos += 1
        inp = [int(x) for x in lines[pos].split()]
        input_tests += [inp]
    return input_tests

if __name__ == "__main__":
    Input = process_input(r'C:\Mtech\COL 100 Python\Python-Lab-COL100\Lab 5\p1_input.txt')
    for inp in Input:
        print(solution(inp))