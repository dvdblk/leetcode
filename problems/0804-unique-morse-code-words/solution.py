class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        """with hash map and set"""
        morse = dict(zip([chr(i) for i in range(ord('a'), ord('z') + 1)], [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]))

        # unique morse representations
        morse_repr = set()


        for word in words:
            morse_word = ""
            for ch in word:
                morse_word += morse[ch]
            morse_repr.add(morse_word)

        return len(morse_repr)

    def uniqueMorseRepresentations2(self, words: List[str]) -> int:
        """DP with set comprehension"""
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        return len(set(["".join([morse[ord(ch)-97] for ch in word]) for word in words]))
