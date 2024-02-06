class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(lambda: [])
        
        for s in strs:
            anagrams["".join(sorted(s))].append(s)
        
        return anagrams.values()
