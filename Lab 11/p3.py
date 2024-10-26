import sys
import math
from functools import lru_cache

def minimum_training_difficulty(A, m):
    """
    Computes the minimum possible difficulty of a training program B,
    which is a subsequence of A with length m+1, starting with 0 and ending with M.
    
    Args:
    - A (List[int]): The original training program list.
    - m (int): The number of training days before the marathon.
    
    Returns:
    - int: The minimum possible difficulty.
    """
    n = len(A) - 1  # Since A has length n+1

    @lru_cache(maxsize=None)
    def helper(last, days):
        """
        Recursive helper function to compute minimum difficulty.
        
        Args:
        - last (int): Current index in A.
        - days (int): Current day in B.
        
        Returns:
        - int: Minimum difficulty up to this point.
        """
        # Base Case: If it's the first day, it must be at index 0
        if days == 0:
            if last == 0:
                return 0
            else:
                return math.inf
        
        # If last is 0 but days > 0, it's invalid
        if last == 0:
            return math.inf
        
        min_difficulty = math.inf
        
        # Iterate over all possible previous indices
        for prev in range(last):
            current_diff = (A[last] - A[prev]) ** 2
            temp = helper(prev, days - 1) + current_diff
            if temp < min_difficulty:
                min_difficulty = temp
        
        return min_difficulty

    # The marathon day must be the last day
    result = helper(n, m)
    
    return result if result != math.inf else -1  # Return -1 if no valid subsequence found
print(minimum_training_difficulty([0,2,1,4,4],4))