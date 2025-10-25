class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        n += 1
        while(not self.balanced(n)):
            n += 1
        return n
    def balanced(self, n: int):
        num = str(n)
        num_dict = {}
        for char in num:
            if (char not in num_dict):
                num_dict[char] = 0
            num_dict[char] += 1

        for key, value in num_dict.items():
            if (int(key) != value):
                return False
        return True
        