from operator import xor

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        ans=0
        for i in range(n):
            nums.append(start+2*i)
        for i in nums:
            ans=xor(ans,i)
        return ans    

if __name__ == "__main__":
    s = Solution()
    n = 5
    start = 0
    print(s.xorOperation(n, start))
