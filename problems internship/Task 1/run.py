#running sum of 1-D array
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res=[]
        sum=0
        for i in nums:
            sum=sum+i
            res.append(sum)
        return res

# Example usage:
if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 9, 4]
    print(sol.runningSum(nums))  # Expected output: [1, 3, 6, 10]
