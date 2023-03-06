

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_1=max(nums)
        nums.remove(max_1)
        max_2=max(nums)
        return (max_1-1)*(max_2-1)

if __name__ == '__main__':
    nums = [8,4,1,2]
    solution = Solution()
    print(solution.maxProduct(nums)) # Expected output: 12
