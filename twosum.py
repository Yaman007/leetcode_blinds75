'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        scannedNums = {}
        for i in range(len(nums)):
            n1 = nums[i]
            n2 = target - nums[i]
            if n2 in scannedNums.keys():
                j = scannedNums[n2]
                return [i, j]
            else:
                scannedNums[n1] = i
        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    answer = solution.twoSum(nums, target)
    print('answer = ', answer)


    nums = [3, 2, 4]
    target = 6
    answer = solution.twoSum(nums, target)
    print('answer = ', answer)

    nums = [3, 3]
    target = 6
    answer = solution.twoSum(nums, target)
    print('answer = ', answer)
