def maximum_reward(A):
    #Input: a matrix A, with positive values, given in the form of a list of lists
    
    # Write your code below to return the maximum possible reward of the robot, as
    # described in the problem statement
    return -1
    

def solution(inp):
    return maximum_reward(inp)

def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines]
    pos = 0
    num_tests = int(lines[0])
    input_tests = []
    for t in range(num_tests):
        pos += 1
        n, m = map(int, lines[pos].split())
        A = [[0] * m for i in range(n)]
        for i in range(n):
            pos += 1
            row_i = [int(x) for x in lines[pos].split()]
            for j in range(m):
                A[i][j] = row_i[j]
        input_tests += [A]
    return input_tests

if __name__ == "__main__":
    Input = process_input('p2_input.txt')
    for inp in Input:
        print(solution(inp))