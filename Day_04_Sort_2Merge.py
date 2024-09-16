"""
Author: V S S L Deepak Janapa

Day - 04
Problem: You are given two sorted arrays arr1 of size m and arr2 of size n.
Your task is to merge these two arrays into a single sorted array without using 
any extra space (i.e., in-place merging). The elements in arr1 should be merged first, 
followed by the elements of arr2, resulting in both arrays being sorted after the merge.

"""
import time
def merge(arr1, arr2, m, n):
    for i in range(m):
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]
            first = arr2[0]
            j = 1
            while j < n and arr2[j] < first:
                arr2[j - 1] = arr2[j]
                j += 1
            arr2[j - 1] = first

#Example
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
m = len(arr1)
n = len(arr2)

start_time = time.time()
merge(arr1, arr2, m, n)
end_time = time.time()
print("Merged arr1:", arr1)
print("Merged arr2:", arr2)
print(f"Time taken for Execution of the sort_arr function is: {end_time-start_time}ms")
