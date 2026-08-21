"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution
of which the time complexity is O(n log(n)).
"""


"""
Same approach but extra space code:

from collections import deque

def min_size(target, nums):
    if target in nums: return 1

    if sum(nums) < target: return 0

    window = deque()
    num_length = len(nums)
    min_length = num_length + 1
    temp_target = target
    i = 0

    while i < num_length:
        diff = temp_target - nums[i]
        window.append(nums[i])

        if diff <= 0:
            while True:
                if diff + window[0] > 0:
                    break
                else:
                    diff += window[0]
                    temp_target += window[0]
                    window.popleft()

            min_length = min(min_length, len(window))

        temp_target -= nums[i]
        i += 1

    return 0 if min_length == num_length else min_length

"""

def min_size(target, nums):
    left = 0
    current_sum = 0
    num_length = len(nums)
    min_length = num_length + 1

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if min_length == num_length + 1 else min_length

target = 15
nums = [1, 2, 3, 4, 5]
# target = 7
# nums = [2,3,1,2,4,3]
print(min_size(target, nums))