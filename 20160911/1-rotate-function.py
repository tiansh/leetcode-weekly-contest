class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0: return 0
        s = sum(A)
        c = 0
        l = len(A)
        z = zip(range(l), A)
        for (i, n) in z:
            c += i * A[i]
        m = c
        for n in A:
            c += l * n - s
            if c > m: m = c
        return m

