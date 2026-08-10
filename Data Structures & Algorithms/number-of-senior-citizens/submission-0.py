class Solution:
    def countSeniors(self, details: List[str]) -> int:
        total = 0
        for citizen in details:
            age = int(citizen[11:13])
            if age > 60:
                total += 1
        return total