import numpy as np

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        my_bool_list =[]
        max_candies=max(candies)
        for i in candies:
            if(extraCandies+i>=max_candies):
                my_bool_list.append(True)
            else:
                my_bool_list.append(False)
        return my_bool_list

# Example usage:
if __name__ == '__main__':
    sol = Solution()
    candies = list(map(int, input().split()))
    extraCandies = int(input())
    print(sol.kidsWithCandies(candies, extraCandies))
