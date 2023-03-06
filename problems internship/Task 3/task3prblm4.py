#. Number of Steps to Reduce a Number to Zero
class Solution:
    def numberOfSteps(self, num: int) -> int:
        c = 0
        if num == 0:
            return 0
        while num >= 0:
            if num % 2 == 0 and num > 0:
                num = num / 2
                c = c + 1
            else:
                num = num - 1
                c = c + 1
            if num == 0:
                break
        return c

# Create an instance of the Solution class
sol = Solution()

# Example usage
num = 14
result = sol.numberOfSteps(num)

print(result) 
    
