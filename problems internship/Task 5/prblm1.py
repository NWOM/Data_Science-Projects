from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [subset + [num] for subset in result]
        return result

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    result = solution.subsets(nums)
    print(result)
