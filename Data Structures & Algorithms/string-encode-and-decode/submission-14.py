class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            length_s = str(len(s))
            result += length_s + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            number = int(s[i:j])
            string = ""
            for temp in range(j + 1, j + number + 1):
                string += s[temp]
            result.append(string)
            i = j + number + 1
        
        return result

sol = Solution()

test = ["Hello", "World"]

encoded = sol.encode(test)

print(encoded)