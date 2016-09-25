class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if len(heightMap) == 0 or len(heightMap[0]) == 0: return 0
        y, x = len(heightMap), len(heightMap[0])
        queue = (
            [(0, i) for i in range(y)] +
            [(x - 1, i) for i in range(y)] +
            [(i, 0) for i in range(x)] +
            [(i, y - 1) for i in range(x)]
        )
        level = [[1000000] * x for i in range(y)]
        for i in range(x):
            for j in range(y):
                if (i, j) in queue: level[j][i] = heightMap[j][i]
        while len(queue):
            i, j = queue.pop(0)
            if i > 0:
                n = max(heightMap[j][i - 1], min(level[j][i - 1], level[j][i]))
                if level[j][i - 1] != n:
                    level[j][i - 1] = n
                    queue.append((i - 1, j))
            if i < x - 1:
                n = max(heightMap[j][i + 1], min(level[j][i + 1], level[j][i]))
                if level[j][i + 1] != n:
                    level[j][i + 1] = n
                    queue.append((i + 1, j))
            if j > 0:
                n = max(heightMap[j - 1][i], min(level[j - 1][i], level[j][i]))
                if level[j - 1][i] != n:
                    level[j - 1][i] = n
                    queue.append((i, j - 1))
            if j < y - 1:
                n = max(heightMap[j + 1][i], min(level[j + 1][i], level[j][i]))
                if level[j + 1][i] != n:
                    level[j + 1][i] = n
                    queue.append((i, j + 1))
        result = 0
        for i in range(x):
            for j in range(y):
                result += level[j][i] - heightMap[j][i]
        return result


