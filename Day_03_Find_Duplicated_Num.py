"""
Author: V S S L Deepak Janapa

Day - 01
Problem: Find the duplicate number
You are given an array arr containing n+1 integers, 
where each integer is in the range [1, n] inclusive. 
There is exactly one duplicate number in the array, but it may appear more than once. 
Your task is to find the duplicate number without modifying the array and using constant extra space.

"""
import time
def find_duplicated(arr):
    n = len(arr)
    temp = []
    for i in range(0,n):
        if arr[i] in temp:
            print(arr[i])
        else:
            temp.append(arr[i])
arr = list(map(int, input("Enter elements of array: ").split()))
start_time = time.time()
find_duplicated(arr)
end_time = time.time()
print(f"Time taken for Execution is: {end_time-start_time}ms")
