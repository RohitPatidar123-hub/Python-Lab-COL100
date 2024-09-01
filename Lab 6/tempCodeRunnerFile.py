def matrix_transpose(A):
    matrix = []
    # Perform matrix transpose
    # for i in range(len(A)):  ##row
    #     C=[]
    #     for j in range(len(A[0])): ##col
        #     C.append(A[j][i])
        # matrix.append(C)   
    matrix=[[A[j][i] for i in range(len(A))] for j in range(len(A[0]))]    #

    return matrix

############################ Do Not Change #################################

def solution(inp):
    return matrix_transpose(inp)

def process_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    pos = 0
    num_tests = int(lines[pos])  # First line contains the number of test cases
    pos += 1
    input_tests = []

    for _ in range(num_tests):
        # Read matrix dimensions
        m, n = map(int, lines[pos].split())  # Read dimensions m and n
        pos += 1

        # Read the matrix rows
        matrix = []
        for _ in range(m):
            row = list(map(int, lines[pos].split()))
            matrix.append(row)
            pos += 1
        
        input_tests.append(matrix)  # Append the matrix to input_tests

    return input_tests

if __name__ == "__main__":
    Input = process_input(r'C:\Mtech\COL 100 Python\Python-Lab-COL100\Lab 6\p2_input.txt')

    # Iterate over each test case input and print the result
    for inp in Input:
        result = solution(inp)
        for row in result:
            print(" ".join(map(str, row)))