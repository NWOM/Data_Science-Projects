from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        answer = 0
        for a,b in zip(startTime,endTime):
            if a <= queryTime <= b:
                answer +=1

        return answer


sol = Solution()

# Example usage
start_times = [9, 8, 7, 6, 5]
end_times = [10, 10, 10, 10, 10]
query_time = 9

result = sol.busyStudent(start_times, end_times, query_time)

print(result) 
