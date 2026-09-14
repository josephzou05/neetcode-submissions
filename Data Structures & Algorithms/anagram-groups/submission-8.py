class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for s in strs:
            characterMap = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                characterMap[index] += 1
            key = tuple(characterMap)
            my_dict[key].append(s)
        
        return list(my_dict.values())
