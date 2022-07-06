'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
[-5, 4, -3, 4]

Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = None
        sigma = nums[0]
        for i in range(1, len(nums)):
            sigma += nums[i]
            if sigma < 0:
                sigma = nums[i]



        return sigma


if __name__ == '__main__':
    solution = Solution()

    nums = [-2,1,-3,4,-1,2,1,-5,4]
    answer = solution.maxSubArray(nums)
    print('answer = ', answer)

    nums = [5,4,-1,7,8]
    answer = solution.maxSubArray(nums)
    print('answer = ', answer)
