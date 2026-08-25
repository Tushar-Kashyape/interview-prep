"""
448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an
array of all the integers in the range [1, n] that do not appear in nums.


Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]


Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n


Follow up: Could you do it without extra space and in O(n) runtime? You may assume
the returned list does not count as extra space.
"""

"""
Approach with extra-space:

def find_missing_nums(nums: list[int]) -> list[int]:
    seen = set(nums)
    n = len(nums)

    return [i for i in range(1, n + 1) if i not in seen]
    
Follow-up: O(n) without extra-space... -> in-place modification

# TOOK HELP for this:
nums -> nums[i] in range [1, n] -> indexing [0, n - 1]
** marking num in nums seen somehow without extra space is the key **
"""

def find_missing_nums(nums: list[int]) -> list[int]:
    n = len(nums)
    ans =[]

    for i in range(n):
        a = abs(nums[i]) - 1

        if nums[a] > 0: nums[a] *= -1

    for i in range(n):
        if nums[i] > 0:
            ans.append(i + 1)

    return ans


n = int(input("Enter number b/w 1 <= n <= 105: "))
nums = list(map(int, input("Enter nums from 1 to n: ").split()))
print(find_missing_nums(nums))