class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        mul=1
        
        while(n>0):

            d=n%10
            sum=sum+d
            mul=mul*d
            n=n//10
        sub=mul-sum
        return sub  
if __name__ == "__main__":
    s = Solution()
    n = 234
    print(s.subtractProductAndSum(n)) # expected output: 15
