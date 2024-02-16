class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        sorted_vals = deque(sorted(c.items(), key=lambda x: x[1]))
        while k > 0:
            key, n_occ = sorted_vals.popleft()
            k -= n_occ

        return len(sorted_vals) + (k != 0)
