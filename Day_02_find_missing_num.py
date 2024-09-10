import time

def find_missing_num(arr):
    min_val = min(arr)
    max_val = max(arr)
    sum_of_expected_range = (max_val*(max_val+1))//2 - (min_val*(min_val-1))//2
    sum_of_arr = sum(arr)
    missing_num = sum_of_expected_range - sum_of_arr
    if missing_num == 0:
        print(f"Missing Number in the array: {max_val+1}")
    else:
        print(f"Missing Number in the array: {missing_num}")

arr = list(map(int, input("Enter the array elements separated by space: ").split()))
start_time = time.time()
find_missing_num(arr)
end_time = time.time()
print(f"Time taken to execute the function: {(end_time - start_time) * 1000:.4f}ms")
