import collections

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if s == "": return 0
        count = collections.Counter(s)
        if min(count.values()) >= k: return len(s)
        p = ""
        m = 0
        for c in s:
            if count[c] >= k: p = p + c
            else:
                if p != "":
                    m = max(m, self.longestSubstring(p, k))
                p = ""
        m = max(m, self.longestSubstring(p, k))
        return m

