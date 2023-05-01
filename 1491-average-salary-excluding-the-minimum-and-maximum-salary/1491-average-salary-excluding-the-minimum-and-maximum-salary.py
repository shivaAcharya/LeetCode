class Solution:
    def average(self, salary: List[int]) -> float:
        N = total_salary = 0
        min_salary, max_salary = float("inf"), float("-inf")
        
        for sal in salary:
            if sal < min_salary:
                min_salary = sal
            if sal > max_salary:
                max_salary = sal
            
            N += 1
            total_salary += sal
        
        return (total_salary - min_salary - max_salary) / (N - 2)