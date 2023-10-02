from typing import List


class Solution:
    def rotate_1(self, nums: List[int], k: int) -> None:
        """
        Rotate by copying the original list.

        Note:
            Time: O(n)
            Space: O(n)
        """
        if len(nums) < 2:
            return
        if k >= len(nums):
            k = k % len(nums)
        if k == 0:
            return

        _nums = nums.copy()
        for i in range(len(nums)):
            nums[(i + k) % len(nums)] = _nums[i]

    def rotate_2(self, nums: List[int], k: int) -> None:
        """
        Rotate by reversing three times with array slicing.

        Note:
            Time: O(n)
            Space: O(1)
        """
        if len(nums) < 2:
            return
        if k >= len(nums):
            k = k % len(nums)
        if k == 0:
            return

        ## Triple reversal via slicing (O(n))
        for i, v in enumerate(nums[::-1]):
            nums[i] = v

        for i, v in enumerate(nums[k - 1 :: -1]):
            nums[i] = v

        for i, v in enumerate(nums[: k - 1 : -1]):
            nums[k + i] = v

    def rotate_3(self, nums: List[int], k: int) -> None:
        """
        Rotate by reversing three times.

        Note:
            Time: O(n)
            Space: O(1)
        """
        if len(nums) < 2:
            return
        if k >= len(nums):
            k = k % len(nums)
        if k == 0:
            return

        ## Triple reversal (O(n))
        # Rotate entire list
        for i in range(int(len(nums) / 2)):
            tmp = nums[i]
            nums[i] = nums[len(nums) - 1 - i]
            nums[len(nums) - 1 - i] = tmp

        # Rotate two sublists
        for i in range(int(k / 2)):
            tmp = nums[i]
            nums[i] = nums[k - 1 - i]
            nums[k - 1 - i] = tmp

        j = 0
        for i in range(int((len(nums) - k) / 2)):
            tmp = nums[k + i]
            nums[k + i] = nums[len(nums) - 1 - j]
            nums[len(nums) - 1 - j] = tmp
            j += 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        if len(nums) < 2:
            return
        if k >= len(nums):
            k = k % len(nums)
        if k == 0:
            return
        ## Cyclic rotation: space O(1), time O(n)
        # Current index (pointer / position)
        ptr = 0
        # Index for tracking factors of k
        i = 0
        # Previous value
        prev = nums[-k % len(nums)]
        for _ in range(len(nums)):
            # Compute the idx to replace
            idx = (ptr + i * k) % len(nums)
            # Swap the value at idx with previous
            _tmp = nums[idx]
            nums[idx] = prev
            prev = _tmp

            i += 1
            # If the cycle is complete (next idx == ptr)
            if ptr == (ptr + i * k) % len(nums):
                # Bump ptr by one and attempt to finish the next cycle (if it exists)
                i = 0
                ptr += 1
                prev = nums[(ptr - k) % len(nums)]
