"""
Author: V S S L Deepak Janapa

Day - 01
Problem: Sort an Array of 0s, 1s, and 2s
You are given an array arr consisting only of 0s, 1s, and 2s. Th 
task is to sort the array in increasing order in linear time (i.e., 
O(n)) without using any extra space. This means you need to 
rearrange the array in-place.

"""

import time
def sort_arr(arr):
    low = 0
    mid = 0
    n = len(arr)
    maxi = n - 1
    
    while mid <= maxi:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[maxi], arr[mid] = arr[mid], arr[maxi]
            maxi -= 1
            
arr = [0, 1, 2, 1, 0, 2, 1, 0]
start_time = time.time()
sort_arr(arr)
end_time = time.time()
print(arr)
print(f"Time taken for Execution of the sort_arr function is: {end_time-start_time}ms")
