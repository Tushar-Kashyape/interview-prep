def min_subsets(arr):
    arr.sort()
    subset_cnt = 1

    for i in range(len(arr)-1):
        if arr[i + 1] - arr[i] > 1:
            subset_cnt += 1

    return subset_cnt

arr = [100, 56, 5, 6, 102, 58, 101, 57, 7, 103, 59]
print(min_subsets(arr))