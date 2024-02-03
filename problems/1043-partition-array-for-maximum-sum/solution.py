class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n+1)

        for start in range(n-1, -1, -1):
            max_elem = -1
            max_score = -1
            for end in range(start, min(start+k, n)):
                max_elem = max(max_elem, arr[end])
                score = max_elem * (end-start+1) + dp[end+1]
                max_score = max(max_score, score)
            
            dp[start] = max_score

        return dp[0]
