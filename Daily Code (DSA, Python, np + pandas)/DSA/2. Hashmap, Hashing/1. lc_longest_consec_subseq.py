"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive
elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore,
its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

"""
Took help to validate my approach.

My approach -> look backward/ forward & check set <---- num ---->

Optimized approach -> don't check till (num - 1) in set and check forward only till
                      curr max len.. if it exceeds we get new max len --> longest
            
"""
def longest_consec_subseq(nums: list[int]) -> int:
    longest = 0
    track = set(nums)

    for num in track:
        if (num - 1) not in track:
            length = 1

            while (num + length) in track:
                length += 1

            longest = max(longest, length)

    return longest

nums = list(map(int, input("Enter nums: ").split()))
print(longest_consec_subseq(nums))