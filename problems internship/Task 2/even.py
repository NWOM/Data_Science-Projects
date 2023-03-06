#find the number with even number of digits 
class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count=0
        for i in nums:
            if(len(str(i))%2==0):
                count=count+1
        return count

# Example usage:
if __name__ == '__main__':
    sol = Solution()
    nums = [19,3458,2,63,7896]
    print(sol.findNumbers(nums))
