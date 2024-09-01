Lab 5: 
Generic Instructions for Lab 5
Lab 5 contains three problems, the descriptions of which are provided below. A starter code is provided for each problem: p1.py, p2.py, and p3.py for problems 1,2 and 3, respectively. Each file contains some sections that are necessary for code execution and an editable section where you are expected to write your code. Kindly note that there is a time limit on the execution of all the problems. 

Do not change anything in the non-editable sections; otherwise, you will run into issues.

Running test cases:

You are provided a text file named pno_input.txt. You have to use this file to test your code. The inputs for each problem can be provided in this file. Sample test cases are provided for all problems. You can copy the sample test case from the description to pno_input.txt to run a problem of your choice. The test cases are described as follows: the first line contains the number of test cases in the file. The subsequent lines contain the test cases. You are provided a proccess_input function that reads the test cases. Example: for problem 1, the input file is named p1_input.txt. It contains the following test case input.

2
5 2
8 7

There are 2 test cases, and the contents of the test cases are 5 2, and 8 7 respectively.

Problem 1

Implement a function power_factorial(n, p), that takes n and p as input, where n is a non negative integer and p is a prime number, and returns the largest exponent t, such that p^t divides n! (factorial of n). The required answer is given by Legendre's formula (htts://en.wikipedia.org/wiki/Legendre%27s_formula):

floor(n/p) + floor(n/p^2) + floor(n/p^3) + ... 

Sample Test case

2
5 2
8 7

In the first testcase of the above example, 5! equals 120, and the largest exponent of 2, that divides 120 is 3 (120 = 2^3 * 15), so you should return 3. 

Problem 2

Implement a function power_binomial(n, k, p), that takes n, k and p as input, where 0 <= k <= n and p is a prime, and returns the largest exponent t, such that p^t divides C(n, k) = n!/(k! (n-k)!).

You can (and ideally should) use the function power_factorial that you implemented in the previous problem.

Sample test case

2
5 3 3
21 7 5

Problem 3

Implement a function power_binomial_360(n, k), that takes integers n and k as input, where k <= n and returns the largest exponent t, such that 360^t divides C(n, k).

You can (and ideally should) use the function power_binomial that you implemented in the previous problem.

Sample test case

2
5 3
21 7