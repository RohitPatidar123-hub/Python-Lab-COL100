def distinct_frequencies(L):
    # The input to the function is a list L
    # The function should return a list of distinct frequencies of the elements in L
    # Write your code here
    fre={}
    for i in L :
        if(i in fre):
             fre[i]=fre[i]+1
        else :
            fre[i]=1
    d={}
    for i in fre :
        d[fre[i]]=1
    return 1
    
def solution(inp):
    return sorted(distinct_frequencies(inp))

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
    Input = process_input('p3_input.txt')
    for inp in Input:
        print(solution(inp))