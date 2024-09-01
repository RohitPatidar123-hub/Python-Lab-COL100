def count_vowels_consonants(text):
    vowel_count = 0
    consonant_count = 0
    
    #Write your code here
    return (vowel_count, consonant_count)
    
    ############################ Do Not Change #################################

def solution(inp):
    return count_vowels_consonants(*inp)

def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines]
    pos = 0
    num_tests = int(lines[0])
    input_tests = []
    for t in range(num_tests):
        pos += 1
        input_tests += [[lines[pos]]]
    return input_tests

if __name__ == "__main__":
    Input = process_input('p4_input.txt')
    for inp in Input:
        print(solution(inp))
