# Copy the functions power_factorial and power_binomial from problem 2
def power_factorial(n, p):
    # Write your code here
    pow=1
    sum=0
    while n//p**pow:
        sum=sum+n//p**pow
        pow=pow+1
    return sum 
def power_binomial(n, k, p) :
     # Write your code here
     a=power_factorial(n, p)
     b=power_factorial(k, p)
     c=power_factorial(n-k, p)
     return a-(b+c)
def power_binomial_360(n, k):
    # Write your code here
    a=power_binomial(n,k,2)//3
    b=power_binomial(n,k,3)//2
    c=power_binomial(n,k,5)//1
    return min(a,b,c)


def solution(inp):
    return power_binomial_360(inp[0], inp[1])

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
    Input = process_input(r'C:\Mtech\COL 100 Python\Python-Lab-COL100\Lab 5\p3_input.txt')
    for inp in Input:
        print(solution(inp))