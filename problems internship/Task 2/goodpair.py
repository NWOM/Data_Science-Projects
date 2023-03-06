#no of good ppairs
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        count = 0
        for f in freq.values():
            count += f*(f-1)//2
        
        return count

# Example usage:
if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,1,1,3]
    print(sol.numIdenticalPairs(nums))
