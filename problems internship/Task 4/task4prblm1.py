from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lmt=[]
        for i in nums:
            if i not in lmt:
                lmt.append(i)
            else:
                lmt.remove(i)
        for j in lmt:
            return j
if __name__ == '__main__':
    solution = Solution()
    nums = [2, 2, 1, 1, 5]
    result = solution.singleNumber(nums)
    print(result)
