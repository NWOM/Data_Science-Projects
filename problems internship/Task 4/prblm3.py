from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        gt=[]
        for i in nums:
            if i not in gt:
                gt.append(i)
            else:
                gt.remove(i)
        
        return gt

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 1, 3, 2, 5]
    result = solution.singleNumber(nums)
    print(result)
