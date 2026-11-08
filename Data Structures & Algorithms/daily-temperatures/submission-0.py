class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        days = [0]* n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                previousDay = stack.pop()
                days[previousDay] = i - previousDay
            
            stack.append(i)
        

        return days


        