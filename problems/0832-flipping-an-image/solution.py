class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = list(map(lambda n: int(not n), image[i][::-1]))

        return image

    def flipAndInvertImage2(self, image: List[List[int]]) -> List[List[int]]:
        """two pointer"""
        for i in range(len(image)):
            left = 0
            right = len(image[i]) - 1
            while left <= right:
                # flip horizontally and invert bits (XOR 1)
                image[i][left], image[i][right] = image[i][right]^1, image[i][left]^1
                left += 1
                right -= 1

        return image