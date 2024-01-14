class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # lengths must match
        if len(s) != len(goal):
            return False

        if s == goal:
            # if they are the same string, check number of occurences of most common character
            return not Counter(s).most_common(1)[0][1] == 1

        # check if there are only two differences at most that can be swapped
        differences = [(l1, l2) for l1, l2 in zip(s, goal) if l1 != l2]
        return len(differences) == 2 and differences[0] == differences[1][::-1]
