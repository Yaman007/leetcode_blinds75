'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numSet = set(nums)
        if len(numSet) != len(nums):
            return True
        return False


if __name__ == '__main__':
    solution = Solution()

    nums = [1,2,3,4]
    answer = solution.containsDuplicate(nums)
    print('answer = ', answer)

    nums = [1,1,1,3,3,4,3,2,4,2]
    answer = solution.containsDuplicate(nums)
    print('answer = ', answer)
