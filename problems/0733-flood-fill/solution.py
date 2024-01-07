class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]

        def bfs(x, y):
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[x]):
                return

            if starting_color != image[x][y] or image[x][y] == color:
                return

            image[x][y] = color
            bfs(x-1, y)
            bfs(x+1, y)
            bfs(x, y-1)
            bfs(x, y+1)


        bfs(sr, sc)
        return image
