from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def count_bits(n):
            return bin(n).count('1')

        return sorted(arr, key=lambda x: (count_bits(x), x))

if __name__ == '__main__':
    solution = Solution()
    arr = [3, 5, 1, 2, 8]
    result = solution.sortByBits(arr)
    print(result)
