class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            order = [0] * 26

            for c in s:
                order[ord(c) - ord('a')] += 1
            groups[tuple(order)].append(s)
        return(list(groups.values()))