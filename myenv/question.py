import pytest

def solution(A, X):
    N = len(A)
    if N == 0:
        return -1
    l = 0
    r = N - 1
    while l <= r:
        m = (l + r) // 2
        if A[m] > X:
            r = m - 1
        else:
            l = m + 1
    if l > 0 and A[l-1] == X:
        return l-1
    return -1
"""
def test_solution():
    # Test case 1: Element is present in the array
    assert solution([1, 2, 5, 9, 11], 11) == 4
    
    # Test case 2: Element is not present in the array
    assert solution([1, 2, 5, 9, 9], 3) == -1
    
    # Test case 3: Element is the first element in the array
    assert solution([1, 2, 5, 9, 9], 1) == 0
    
    # Test case 4: Element is the last element in the array
    assert solution([1, 2, 5, 9, 9], 9) in [3, 4]
    
    # Test case 5: Array is empty
    assert solution([], 5) == -1
    
    # Test case 6: Array contains one element which is the search key
    assert solution([5], 5) == 0
    
    # Test case 7: Array contains one element which is not the search key
    assert solution([1], 5) == -1
    
    # Test case 8: All elements are the same and equal to the search key
    assert solution([5, 5, 5, 5, 5], 5) in range(5)
    
    # Test case 9: All elements are the same but not equal to the search key
    assert solution([1, 1, 1, 1, 1], 5) == -1

if __name__ == "__main__":
    pytest.main()

"""