class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 2:
            return False

        incr = arr[0] < arr[1]
        if not incr:
            return False

        for i in range(1, len(arr)):
            if incr and arr[i] <= arr[i-1]:
                incr = False
                if arr[i] == arr[i-1] and i == len(arr) - 1:
                    return False
            elif not incr and arr[i] >= arr[i-1]:
                return False

        return not incr