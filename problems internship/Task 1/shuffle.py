#shuffle the array
class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        ls1=[]
        for i in range(n):
            ls1.append(nums[i])
            ls1.append(nums[n+i])
        return ls1

# Example usage:
if __name__ == '__main__':
    sol = Solution()
    nums = list(map(int, input().split()))
    n = int(input())
    print(sol.shuffle(nums, n))
