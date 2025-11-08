class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        i = 0
        negative = False
        if (x < 0):
            x *= -1
            negative = True
        while(x > 0):
            left_digit = x % 10
            x = x // 10
            if res > 214748364 or (res == 214748364 and left_digit > (7 if not negative else 8)):
                return 0
            res = res * 10 + left_digit

        if(negative):
            return res * -1
        return res
        