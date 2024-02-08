class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = n

        def dfs(node):
            # skip node if already visited
            nonlocal provinces
            if visited[node]:
                return
            visited[node] = True

            for i in range(len(isConnected)):
                # visit all adjacent nodes
                if isConnected[i][node] and not visited[i]:
                    # start dfs from visited node
                    dfs(i)
                    # this edge decreases the amnt of provinces
                    provinces -= 1

        # start dfs from each node
        for i in range(n):
            dfs(i)

        return provinces
