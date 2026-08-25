"""
3471. Find the Largest Almost Missing Integer

You are given an integer array nums and an integer k.

An integer x is almost missing from nums if x appears in exactly one subarray of
size k within nums.

Return the largest almost missing integer from nums. If no such integer exists,
return -1.

A subarray is a contiguous sequence of elements within an array.


Example 1:

Input: nums = [3,9,2,1,7], k = 3

Output: 7

Explanation:

1 appears in 2 subarrays of size 3: [9, 2, 1] and [2, 1, 7].
2 appears in 3 subarrays of size 3: [3, 9, 2], [9, 2, 1], [2, 1, 7].
3 appears in 1 subarray of size 3: [3, 9, 2].
7 appears in 1 subarray of size 3: [2, 1, 7].
9 appears in 2 subarrays of size 3: [3, 9, 2], and [9, 2, 1].
We return 7 since it is the largest integer that appears in exactly one subarray
of size k.

Example 2:

Input: nums = [3,9,7,2,1,7], k = 4

Output: 3

Explanation:

1 appears in 2 subarrays of size 4: [9, 7, 2, 1], [7, 2, 1, 7].
2 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
3 appears in 1 subarray of size 4: [3, 9, 7, 2].
7 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
9 appears in 2 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1].
We return 3 since it is the largest and only integer that appears in exactly one
subarray of size k.

Example 3:

Input: nums = [0,0], k = 1

Output: -1

Explanation:

There is no integer that appears in only one subarray of size 1.

Constraints:

1 <= nums.length <= 50
0 <= nums[i] <= 50
1 <= k <= nums.length
"""

"""
Testcases failed 2-3 times because of unnecessary optimization - removing repeated
keys from dictionary which altered the real count tracking.

Kept it simple and check on occurrence in the end.
"""

def largest_almost_missing(nums: list[int], k: int) -> int:
    n = len(nums)
    num_freq = {}
    largest_missing = -1

    if k == n: return max(nums)

    i = 0
    while i + k <= n:
        for j in range(i, i + k):
            if nums[j] in num_freq:
                num_freq[nums[j]] += 1
            else:
                num_freq[nums[j]] = 1
        i += 1

    for k,v in num_freq.items():
        if v == 1:
            largest_missing = max(largest_missing, k)

    return largest_missing

nums = list(map(int, input("Enter nums: ").split()))
k = int(input("Enter k: "))
# nums = [2,10,8,2,0]
# k = 3
print(largest_almost_missing(nums, k))