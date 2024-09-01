def min_operations_to_make_similar(s1, s2):
    operations = 0
    
    #Write your code here
    return operations
    
    
    ############################ Do Not Change #################################

def solution(inp):
    s1, s2 = inp  # Each input is a pair of strings
    return min_operations_to_make_similar(s1, s2)

def process_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    num_tests = int(lines[0].strip())
    input_tests = []
    
    for i in range(1, num_tests + 1):
        # Each line contains two strings separated by a comma
        s1, s2 = lines[i].strip().split(',')
        input_tests.append((s1.strip('"'), s2.strip('"')))
    
    return input_tests

if __name__ == "__main__":
    Input = process_input('p5_input.txt')
    
    # For each test case, compute the result
    for inp in Input:
        print(solution(inp))