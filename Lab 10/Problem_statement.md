Lab 10: 
Generic Instructions for Lab 10
Lab 10 contains three problems, the descriptions of which are provided below. A starter code is provided for each problem: p1.py, p2.py and p3.py for problems 1, 2, and 3, respectively. Each file contains some sections that are necessary for code execution and an editable section where you are expected to write your code. Kindly note that there is a time limit on the execution of all the problems. 

Do not change anything in the non-editable sections; otherwise, you will run into issues.

Running test cases:

You are provided a text file named pno_input.txt. You have to use this file to test your code. The inputs for each problem can be provided in this file. Sample test cases are provided for all problems. You can copy the sample test case from the description to pno_input.txt to run a problem of your choice. The test cases are described as follows: the first line contains the number of test cases in the file. The subsequent lines contain the test cases. You are provided a proccess_input function that reads the test cases. Example: for problem 1, the input file is named p1_input.txt.

Problem 1

Kindly note that this problem was also used in Lab 7. The difference however is that, here, the inputs will be large, and the solutions that do not use memoization will fail!

Implement a function num_ways(R, G, B), that takes as input R, G and B, and returns the number of ways to arrange R identical red balls, G identical green balls and B identical blue balls in a line such that no two consecutive balls have the same color.

For example, If R = 1, G = 2, B = 1, the following are the valid ways:

1. RGBG
2. BGRG
3. GBRG
4. GRBG
5. GRGB
6. GBGR

Hence, num_ways(1, 2, 1)  should return 6.
 
Sample Input:
2
1 2 1
0 2 2
 
Sample Output:
6
2
 
 
Problem 2

Kindly note that this problem was also used in Lab 7. The difference however is that, here, the inputs will be large, and the solutions that do not use memoization will fail!

You are given a matrix A, consisting of n rows and m columns. The rows of A are numbered 0, 1, 2, .. n-1 from top to bottom, and the columns are numbered 0, 1, ..., m - 1, from left to right. We will use (i, j) to represent the cell with row number i, and column number j. For every row i, and column j, there is a reward of A[i][j] available in the cell (i, j).

You have a robot, currently placed at (0, 0). You want to make it reach (n, m), while collecting the maximum possible reward. In every move, the robot can either move one step down or one step right. That is, from a cell (i, j), the robot can either move to (i + 1, j), or to the cell (i, j + 1), with the additional constraint that it can not get out of the matrix. For example, if n = 3, m = 4, it is not allowed to go from (2, 2)  to (3, 2), since there is no cell (3, 2) in the matrix.

Write a function maximum_reward(A), that takes the matrix A as input and returns the maximum possible reward that can be collected.

For example, consider the following matrix, with 2 rows and 3 columns

3 1 6
4 1 1

Here, there are two possible paths that the robot might take:

1. (0, 0) -> (1, 0) -> (1, 1) -> (1, 2) : Here, the total reward is 3 + 4 + 1 + 1 = 9
2. (0, 0) -> (0, 1) -> (0, 2) -> (1, 2) : Here, the total reward is 3 + 1 + 6 + 1 = 11

Hence, maximum_reward([[3, 1, 6], [4, 1, 1]]) must return 11.
 
Sample Input:
2
2 2
1 2
3 4
2 3
3 1 6
4 1 1

Sample Output:
8
11


Problem 3
 
Implement a function distinct_frequencies(L), that takes list L of integers as input, and returns a list of the distinct frequencies of the values in L.

For example, if L = [7, 1, 1, 8, 7, 3, 3, 3, 3]:
    - The value 1 appears twice
    - The value 3 appears 4 times
    - The value 7 appears twice
    - The value 8 appears once

Hence, the list of distinct frequencies is [1, 2, 4]. Please note that, any ordering of the output list will be accepted. For example, for the above input, [2, 4, 1] is also treated as a valid return value. However, [1, 2, 2, 4] is not accepted, since the list must only contain the distinct frequencies.
 
Sample Input:
2
1 2 3
7 1 1 8 7 3 3 3 3
 
Sample Output:
[1]
[1, 2, 4]