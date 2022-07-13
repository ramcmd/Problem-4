# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:07:57 2022

@author: 91886
"""
# TC: O(log n)

# =============================================================================
# Binary search implementation
# =============================================================================

arr = [2,3,4,5,6,7,8,9]
num = 9

# =============================================================================
# recursive
# =============================================================================

def BinarySearch(arr, low, high, num):
    if low > high:
        return False
    
    mid = low + (high - low)//2
    
    if arr[mid] == num:
        return True
    
    elif arr[mid] > num:
        return BinarySearch(arr, low, mid -1, num)
    else:
        return BinarySearch(arr, mid +1, high, num)



    
BinarySearch(arr, 0, len(arr)-1, 5)
        
BinarySearch(arr, 0, len(arr)-1, 1)        
BinarySearch(arr, 0, len(arr)-1, 9)       


low = 0
high = len(arr) - 1


# =============================================================================
# Iterative
# =============================================================================

def BSIterative(arr, n, key):
    low = 0
    high = n - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if key == arr[mid]:
            return True
            break
        elif key < arr[mid]:
            high = mid - 1
        
        else:
            low = mid + 1
    
    return False
        
BSIterative(arr, len(arr), 1)
BSIterative(arr, len(arr), 3)
BSIterative(arr, len(arr), 10)
BSIterative(arr, len(arr), 8)


