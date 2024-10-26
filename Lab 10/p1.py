def num_ways(R, G, B):
    # R, G and B are inputs to the function
    # R denotes the number of red balls
    # G denotes the number of green balls
    # B denotes the number of blue balls
    
    # Write your code below to return the number of ways to
    # arrange R red balls, G green balls and B blue balls
    # in a line such that no two consecutive balls have the
    # same color.
    memo={}
    def dp(R,G,B,last) :
        if(R,G,B,last)in memo :
            return memo[(R,G,B,last)]
        if(R==0 and G==0 and B==0):
            return 1
        ways=0
        if(last!='R' and R>0):
            ways+=dp(R-1,G,B,'R')
        if(last!='G'and G>0) :
            ways+=dp(R,G-1,B,'G')  
        if(last!='B'and B>0) :
            ways+=dp(R,G,B-1,'B') 
        memo[(R,G,B,last)]=ways
        return ways    
    return dp(R,G,B,'')
    
print(num_ways(1,2,2))
# def solution(inp):
#     return num_ways(*inp)

# def process_input(filename):
#     lines = open(filename, 'r').readlines()
#     lines = [line.strip() for line in lines]
#     pos = 0
#     num_tests = int(lines[0])
#     input_tests = []
#     for t in range(num_tests):
#         pos += 1
#         inp = [int(x) for x in lines[pos].split()]
#         input_tests += [inp]
#     return input_tests

# if __name__ == "__main__":
#     Input = process_input('p1_input.txt')
#     for inp in Input:
#         print(solution(inp))