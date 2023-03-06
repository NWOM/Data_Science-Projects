#how many numbers ar smaller than the current number 
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        a=[]
        numi = sorted(nums)
        for i in range(0,len(nums)):
            a.append(numi.index(nums[i]))
        return a
def main():
    s = Solution()
    nums = list(map(int, input().split()))
    result = s.smallerNumbersThanCurrent(nums)
    print(result)

if __name__ == '__main__':
    main()
        