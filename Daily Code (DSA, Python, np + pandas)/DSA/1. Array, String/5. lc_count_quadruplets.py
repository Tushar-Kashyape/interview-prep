"""
Given a 0-indexed integer array nums, return the number of distinct quadruplets
(a, b, c, d) such that:

nums[a] + nums[b] + nums[c] == nums[d], and
a < b < c < d

Example 1:

Input: nums = [1,2,3,6]
Output: 1
Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3)
because 1 + 2 + 3 == 6.

Example 2:

Input: nums = [3,3,6,4,5]
Output: 0
Explanation: There are no such quadruplets in [3,3,6,4,5].
Example 3:

Input: nums = [1,1,1,3,5]
Output: 4
Explanation: The 4 quadruplets that satisfy the requirement are:
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5


Constraints:

4 <= nums.length <= 50
1 <= nums[i] <= 100
"""
from collections import defaultdict

"""
Heavy Brute-force:

def count_quadruplet(nums: list[int]) -> int:
    count = 0
    n = len(nums)
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                for d in range(c + 1, n):
                    if nums[a] + nums[b] + nums[c] == nums[d]:
                        count += 1
    return count
"""

def count_quadruplet(nums: list[int]) -> int:
    count = 0
    n = len(nums)
    track = defaultdict(int)

    """
    Requirement: 
    nums[a] + nums[b] + nums[c] == nums[d] i.e. 
    
    nums[a] + nums[b] == nums[d] - nums[c]
    
    So, we will keep track of count for sum of (a + b), and then check whether it 
    is equal to (d - c). Number of times it is true -> count
    
    Prefix-sum category
    """
    for c in range(2, n - 1):
        b = c - 1

        for a in range(b):
            track[nums[a] + nums[b]] += 1

        for d in range(c + 1, n):
            count += track[nums[d] - nums[c]]

    return count

"""
Had to check logic for more optimized solution. Brute-force can work because length
of input array is small.
"""
nums = list(map(int, input("Enter the nums: ").split()))
print(count_quadruplet(nums))