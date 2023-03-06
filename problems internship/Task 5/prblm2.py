class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        d = x ^ y
        q = bin(d).replace("0b", " ")
        return q.count('1')

if __name__ == '__main__':
    solution = Solution()
    x = 1
    y = 4
    result = solution.hammingDistance(x, y)
    print(result)
