class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counts = {}
        
        # Count the number of occurrences of each element
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        
        # Find the element that occurs only once
        for num in counts:
            if counts[num] == 1:
                return num

if __name__ == '__main__':
    solution = Solution()
    nums = [2, 2, 1]
    result = solution.singleNumber(nums)
    print(result)
