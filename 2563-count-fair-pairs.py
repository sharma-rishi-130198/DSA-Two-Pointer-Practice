"""
Problem: 2563. Count the Number of Fair Pairs
Link: https://leetcode.com/problems/count-the-number-of-fair-pairs
Difficulty: Medium

Description:
Given an array of integers nums and two integers lower and upper, return the number of fair pairs.
A pair (i, j) is fair if:
- 0 <= i < j < nums.length, and
- lower <= nums[i] + nums[j] <= upper

Example:
Input: nums = [1,2,5,3], lower = 4, upper = 6
Output: 2
"""

from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs_brute_force(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Time Complexity = O(n^2), Space Complexity = O(1)
        Approach:
            - Iterate over all pairs (i, j) where i < j
            - Check if nums[i] + nums[j] lies within the given [lower, upper] range
            - Increment count if condition is satisfied
        """
        count = 0
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if lower <= nums[i] + nums[j] <= upper:
                    count += 1
        return count

    def countFairPairs_optimal(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Time Complexity = O(n log n), Space Complexity = O(1)
        Approach:
            - Sort the array
            - For each nums[i], use binary search to find the count of valid j's such that:
                lower - nums[i] <= nums[j] <= upper - nums[i]
                with j > i
            - Use bisect_left and bisect_right for efficient range count
        """
        nums.sort()
        count = 0
        n = len(nums)
        for i in range(n):
            low = bisect_left(nums, lower - nums[i], i + 1, n)
            high = bisect_right(nums, upper - nums[i], i + 1, n)
            count += (high - low)
        return count


if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,7,4,4,5]
    lower = 3
    upper = 6

    print("Brute Force:", sol.countFairPairs_brute_force(nums, lower, upper))  # Output: 2
    print("Optimal:", sol.countFairPairs_optimal(nums, lower, upper))          # Output: 2