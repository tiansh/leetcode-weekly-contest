class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = list(num)
        mem = 0
        for i in range(k):
            j = mem
            # remove zeroes
            while len(n) > 0 and [0] == '0': n[0:1] = []
            while j < len(n) - 1:
                if n[j] == n[j + 1]: j += 1
                else:
                    mem = max(0, j - 1)
                    while n[j] <= n[j + 1]:
                        if j == len(n) - 2: break
                        j += 1
                    if n[j] <= n[j + 1]: n[j + 1:j + 2] = []
                    else: n[j:j + 1] = []
                    break
            else:
                n[0:1] = []
                mem = max(0, len(n) - 2)
        while len(n) > 0 and n[0] == '0': n[0:1] = []
        if len(n) > 0: return ''.join(n)
        else: return '0'

