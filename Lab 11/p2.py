def safe_division(numbers, first_index, second_index):
    # Step 1: Handle Index Out of Bound
    try:
        num1 = numbers[first_index]
        num2 = numbers[second_index]
    except :
        return "INDEX OUT OF BOUND"

    # Step 2: Handle Non-Integer Conversion
    try:
        num1 = int(num1)
        num2 = int(num2)
    except :
        return "INVALID NUMBER"

    # Step 3: Handle Division by Zero
   
    try :
        result =round(num1/num2,2)
    except :
          return "DIVISION BY ZERO"  

    # Step 4: Perform division and round to two decimal places
  

# Example Usage:
print(safe_division(["24", "48", "12", "64", "36"], 1, 2))  # Output should be 4.0
print(safe_division(["24", "48", "0", "64", "36"], 1, 2))   # Output should be "DIVISION BY ZERO"
print(safe_division(["24", "48", "0", "64", "36"], 1, 5))   # Output should be "INDEX OUT OF BOUND"
print(safe_division(["24", "48", "0", "64", "AB"], 1, 4))   # Output should be "INVALID NUMBER"
print(safe_division(["24", "AB", "12", "64", "0"], 1, 4))   # Output should be "INVALID NUMBER"
print(safe_division(["24", "AB", "12", "64", "0"], 1, -6))  # Output should be "INDEX OUT OF BOUND"
