Problem 1 :  Squares till n

Given a positive integer n, write a function squares_till_n with input n that returns a list of squares of all positive integers such that the square is less than or equal to n. The list should contain the squares in increasing order.

Sample test case

2
10
20

 

Problem 2 : Matrix Transpose

Given a matrix A of dimensions m x n, the transpose of the matrix A is a matrix B of dimensions n x m such that B[i][j] = A[j][i] for all 0 <= i < n and 0 <= j < m. Write a function matrix_transpose(A) that returns the transpose of the matrix A.

Hint: you can get the size of a matrix A using len(A) and len(A[0]) to get the number of rows and columns respectively.

Sample test case

1
[[1, 2, 3], [4, 5, 6]]


Problem 3 : Remaining Stone Weight

You are given a list of integers stones representing the weights of stones. Each turn, you choose the two heaviest stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and removed from the list
If x != y, the stone of weight x is destroyed, and the stone of weight y - x is left in the list.
At the end of the game, there is at most one stone left. Return the weight of the remaining stone or 0 if there are no stones left.

Write a function last_stone_weight(stones) that takes a list of integers stones as input and returns the weight of the remaining stone.

Sample test case

1
[2, 7, 4, 1, 8, 1]

 

Problem 4: Counting Vowels and Consonants in a String

Write a function count_vowels_consonants(text) that takes a string text as input and returns a tuple containing the count of vowels and consonants in the text. The function should ignore case(treat uppercase and lowercase characters identically) and consider only alphabets as vowels/consonants. The tuple should contain the count of vowels followed by the count of consonants.

Sample test case

1

Hello, World!

Problem 5: Minimum Operations to make strings similar

Two strings s1 and s2 are similar if you can make s1 equal to s2 by rearranging the letters of s1. You are given two strings s1 and s2. Write a function min_operations_to_make_similar(s1, s2) that returns the minimum number of operations required to make s1 and s2 similar. The operations allowed are:

Add a character to s1
Remove a character from s1
Replace a character in s1 with another character
Sample test case
2
abc,bca
abc,def