from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """O(n+m) time and space"""
        d1 = {word: i for i, word in enumerate(list1)}
        d2 = {word: i for i, word in enumerate(list2)}

        min_idx_sum = len(list1) + len(list2)
        min_words = []
        for word in list1:
            index_sum = d1[word] + d2.get(word, min_idx_sum)
            if index_sum == min_idx_sum:
                min_words.append(word)
            elif index_sum < min_idx_sum:
                min_idx_sum = index_sum
                min_words = [word]
        return min_words
