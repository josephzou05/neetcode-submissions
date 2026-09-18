class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for item in operations:
            
            if item == "+":
                summ = stack[-2] + stack[-1]
                stack.append(summ)
            elif item == "D":
                stack.append(2 * stack[-1])
            elif item == "C":
                stack.pop()
            else:
                stack.append(int(item))
        score = 0
        for num in stack:
            score += num
        return score