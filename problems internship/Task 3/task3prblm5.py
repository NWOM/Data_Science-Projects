from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        lst=[]
        for i in range(n+1):
            d=bin(i).count('1')
            lst.append(d)
        return lst
if __name__ == '__main__':
    solution = Solution()
    n = 5
    result = solution.countBits(n)
    print(result)
