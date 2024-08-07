class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        """Two hashmaps"""
        new_s = ""
        # bijective mappings
        mapping, mapping_inv = {}, {}

        for i, ch in enumerate(s):
            # check if current char of s is already mapped
            if new_ch := mapping.get(ch):
                new_s += new_ch
            else:
                mapping[ch] = t[i]
                # for cases when bijective property would break, return False
                if mapping_inv.get(t[i]) is not None:
                    return False
                mapping_inv[t[i]] = ch
                new_s += t[i]

        return new_s == t

    def isIsomorphic2(self, s: str, t: str) -> bool:
        map_s, map_t = {}, {}
        i_s, i_t = 0, 0
        res_s, res_t = "", ""

        for i in range(len(s)):
            if key_s := map_s.get(s[i]):
                res_s += key_s
            else:
                key_s = chr(ord("A") + i_s)
                map_s[s[i]] = key_s
                i_s += 1
                res_s += key_s

            if key_t := map_t.get(t[i]):
                res_t += key_t
            else:
                key_t = chr(ord("A") + i_t)
                map_t[t[i]] = key_t
                i_t += 1
                res_t += key_t

            if key_s != key_t:
                return False

        return True
