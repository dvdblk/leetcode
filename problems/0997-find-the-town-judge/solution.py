class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # find the person that trusts nobody
        trustees = set(range(1, n+1))
        for a, _ in trust:
            if a in trustees:
                trustees.remove(a)

        if len(trustees) == 1:
            trusts_nobody = trustees.pop()

            # verify if everybody trusts him
            n_ppl_that_trust = 0
            for a, b in trust:
                if a != trusts_nobody and b == trusts_nobody:
                    n_ppl_that_trust += 1
            return trusts_nobody if n_ppl_that_trust == n - 1 else -1
        else:
            return -1
