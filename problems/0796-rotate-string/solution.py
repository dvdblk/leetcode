class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            new_str = s[i:] + s[:i]
            if new_str == goal:
                return True

        return False

    def rotateString2(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s