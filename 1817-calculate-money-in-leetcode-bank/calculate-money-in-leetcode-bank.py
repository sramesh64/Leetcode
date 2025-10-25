class Solution:
    def totalMoney(self, n: int) -> int:
        i = 1
        res = 0
        addition = 0
        while(i <= n):
            if(i > 1 and i % 7 == 1):
                addition -= 5
            else:
                addition += 1
            print(addition)
            res += addition
            i += 1
        return res
