"""
1413. Minimum Value to Get Positive Step by Step Sum

Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements
in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is
never less than 1.

Example 1:

Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
step by step sum
startValue = 4 | startValue = 5 | nums
  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
  (4 +2 ) = 6  | (5 +2 ) = 7    |   2
Example 2:

Input: nums = [1,2]
Output: 1
Explanation: Minimum start value should be positive.
Example 3:

Input: nums = [1,-2,-3]
Output: 5


Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
"""

def min_start_value(nums: list[int]) -> int:
    n = len(nums)
    min_diff = 1
    curr_diff = None

    for i in range(n - 1, -1, -1):
        if curr_diff:
            curr_diff -= nums[i]
            if curr_diff < 1: curr_diff = 1
        else:
            if nums[i] < 0:
                curr_diff = min_diff - nums[i]
            else: curr_diff = min_diff

    return curr_diff if curr_diff > 0 else 1

nums = list(map(int, input("Enter nums: ").split()))
print(min_start_value(nums))

"""
One test case failed for [-5 -2 4 4 -2]

Prev Logic: Diff against OR Sum with min. value in nums should be >= 1
            here min. val was -5 -> 6 as start-value but it fails later in nums
New Logic: Diff against OR Sum with last negative value should be >= 1, then
            continue backwards till start of nums -> start-value
"""