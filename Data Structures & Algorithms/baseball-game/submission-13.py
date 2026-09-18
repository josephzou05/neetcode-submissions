class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for item in operations:
            if item == "+":
                num = stack[-2] + stack[-1]
                stack.append(num)
                total += num
            elif item == "D":
                num = 2 * stack[-1]
                stack.append(num)
                total += num
            elif item == "C":
                num = stack[-1]
                stack.pop()
                total -= num
            else:
                num = int(item)
                stack.append(num)
                total += num
        return total