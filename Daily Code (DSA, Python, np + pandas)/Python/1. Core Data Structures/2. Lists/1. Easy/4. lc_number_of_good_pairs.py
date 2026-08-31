"""
1512. Number of Good Pairs

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

Count the number of occurrences for a number. If it is n times then, n * (n - 1)// 2
pairs can be formed.
"""
from collections import Counter


def num_good_pairs(nums: list[int]) -> int:
    ans = 0
    freq = Counter(nums)

    for val in freq.values():
        if val > 0: ans += (val * (val - 1)) // 2

    return ans

nums = list(map(int, input("Enter nums: ").split()))
print(num_good_pairs(nums))