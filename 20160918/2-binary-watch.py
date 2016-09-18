# I know it is very ugly, but it works

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        output = []
        for n1 in range(2):
            if n1 <= num and n1 >= num-9:
                for n2 in range(2):
                    if n1 + n2 <= num and n1 + n2 >= num - 8:
                        for n3 in range(2):
                            if n1 + n2 + n3 <= num and n1 + n2 + n3 >= num - 7:
                               for n4 in range(2):
                                    if n1 + n2 + n3 + n4 <= num and n1 + n2 + n3 + n4 >= num -6:
                                        for n5 in range(2):
                                            if n1 + n2 + n3 + n4 + n5 <= num and n1 + n2 + n3 + n4 + n5 >= num - 5:
                                                for n6 in range(2):
                                                    if n1 + n2 + n3 + n4 + n5 + n6 <= num and n1 + n2 + n3 + n4 + n5 + n6 >= num - 4:
                                                        for n7 in range(2):
                                                            if n1 + n2 + n3 + n4 + n5 + n6 + n7 <= num and  n1 + n2 + n3 + n4 + n5 + n6 + n7 >= num - 3:
                                                                for n8 in range(2):
                                                                    if n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 <= num and n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8  >= num-2:
                                                                        for n9 in range(2):
                                                                            if n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 <= num and n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9  >= num -1:
                                                                                for n10 in range(2):
                                                                                    if n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 == num:
                                                                                        h = n1 * 8 + n2 * 4 + n3 * 2 + n4
                                                                                        m = n5 * 32 + n6 * 16 + n7 * 8 + n8 * 4 + n9 * 2 + n10
                                                                                        if 0 <= h <= 11 and 0 <= m <= 59:
                                                                                            output.append('%d:%02d' % (h, m))
        return output

