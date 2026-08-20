"""
Given an integer array nums and an integer k, return true if there are two distinct
indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""
from flask import Flask


def contains_duplicates(nums, k):
    num_len = len(nums)
    if num_len <= 1: return False

    nums_map, flag = {}, False
    for i in range(num_len):
        if nums[i] in nums_map:
            if abs(nums_map[nums[i]] - i) <= k:
                return True

        nums_map[nums[i]] = i

    return flag


nums = [1,2,3,1,2,3]
k = 2
print(contains_duplicates(nums, k))