##################################################
# Name: Gazi Shuraim Niloy 
# Collaborators:
# Estimate of time spent (hr):
##################################################

def is_magic_square(array: list[list[int]]) -> bool:
    
    n = len(array)
    if not all(len(row) == n for row in array):
        return False  

    
    target_sum = sum(array[0])

    
    for row in array:
        if sum(row) != target_sum:
            return False

    
    for col in range(n):
        if sum(array[row][col] for row in range(n)) != target_sum:
            return False

    
    if sum(array[i][i] for i in range(n)) != target_sum:
        return False

    
    if sum(array[i][n - i - 1] for i in range(n)) != target_sum:
        return False

    
    return True

# Test with the provided example
small = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
print(is_magic_square(small))  
