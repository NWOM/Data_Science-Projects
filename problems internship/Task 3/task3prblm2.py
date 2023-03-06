

class Solution:
    def numTeams(self, rating: list[int]) -> int:
        n = len(rating)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        count += 1
        return count

if __name__ == '__main__':
    rating = [8,5,3,4,9]
    solution = Solution()
    print(solution.numTeams(rating)) 
