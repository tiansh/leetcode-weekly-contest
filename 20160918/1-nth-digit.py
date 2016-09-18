# I know it is ugly, but it works

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 9: return n
        n = n + 9
        if n <= 99 * 2: return int(str(int((n + 1) / 2))[(n + 1) % 2])
        n = n + 99
        if n <= 999 * 3: return int(str(int((n + 2) / 3))[(n + 2) % 3])
        n = n + 999
        if n <= 9999 * 4: return int(str(int((n + 3) / 4))[(n + 3) % 4])
        n = n + 9999
        if n <= 99999 * 5: return int(str(int((n + 4) / 5))[(n + 4) % 5])
        n = n + 99999
        if n <= 999999 * 6: return int(str(int((n + 5) / 6))[(n + 5) % 6])
        n = n + 999999
        if n <= 9999999 * 7: return int(str(int((n + 6) / 7))[(n + 6) % 7])
        n = n + 9999999
        if n <= 99999999 * 8: return int(str(int((n + 7) / 8))[(n + 7) % 8])
        n = n + 99999999
        if n <= 999999999 * 9: return int(str(int((n + 8) / 9))[(n + 8) % 9])
        n = n + 999999999
        if n <= 9999999999 * 10: return int(str(int((n + 9) / 10))[(n + 9) % 10])
        n = n + 9999999999
        if n <= 99999999999 * 11: return int(str(int((n + 10) / 11))[(n + 10) % 11])
        n = n + 99999999999
        if n <= 999999999999 * 12: return int(str(int((n + 11) / 12))[(n + 11) % 12])
        n = n + 999999999999
        if n <= 9999999999999 * 13: return int(str(int((n + 12) / 13))[(n + 12) % 13])
        return ''

s = ''
for i in range(1, 1000):
  s += str(Solution().findNthDigit(i))
print(s)

p = ''
for i in range(1, 370):
  p += str(i)

print(p)

print(s == p)
