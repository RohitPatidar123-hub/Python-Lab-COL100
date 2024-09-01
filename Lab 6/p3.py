def remaining_stone_weight(stones):
    
    #Write your code here
    while len(stones)>1:
          stones.sort()
          a=stones.pop()
          b=stones.pop()
          stones.append(a-b)
    return stones    
############################ Do Not Change #################################

def solution(inp):
    return remaining_stone_weight(inp)

def process_input(filename):
    with open(filename, 'r') as file:
      lines = file.readlines()
    
    num_tests = int(lines[0].strip())
    input_tests = []
    
    for i in range(1, num_tests + 1):
        # Convert each line into a list of integers
        stones = list(map(int, lines[i].strip().strip('[]').split(',')))
        input_tests.append(stones)
    
    return input_tests

if __name__ == "__main__":
    Input = process_input(r'C:\Mtech\COL 100 Python\Python-Lab-COL100\Lab 6\p3_input.txt')
    
    # For each test case, compute the result
    for inp in Input:
        print(solution(inp))