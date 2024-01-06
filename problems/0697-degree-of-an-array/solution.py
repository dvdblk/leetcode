class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """O(n)"""
        # create a dict of
        # key = element
        # value = list of indices of element in nums
        elem_dict = defaultdict(list)
        for i, e in enumerate(nums):
            elem_dict[e].append(i)

        # compute nums degree
        degree = max([len(i) for i in elem_dict.values()])

        # get the shortest subarray path
        n_shortest = len(nums)
        for idxs in elem_dict.values():
            # only check indices where degree matches the length
            if len(idxs) != degree:
                continue
            start, end = idxs[0], idxs[-1]

            n_shortest = min(n_shortest, end - start + 1)

        return n_shortest