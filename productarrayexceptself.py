'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lefthash_product = [1]*len(nums)
        righthash_product = [1]*len(nums)
        answers = []

        for i in range(len(nums)):
            if i >= 1:
                lefthash_product[i] *= lefthash_product[i-1] * nums[i-1]
                righthash_product[len(nums)-i-1] *= righthash_product[len(nums) - i] * nums[len(nums)-i]

        for i in range(len(nums)):
            answers.append(lefthash_product[i] * righthash_product[i])

        return answers


if __name__ == '__main__':
    solution = Solution()

    nums = [1,2,3,4]
    answer = solution.productExceptSelf(nums)
    print('answer = ', answer)

    nums = [-1,1,0,-3,3]
    answer = solution.productExceptSelf(nums)
    print('answer = ', answer)
