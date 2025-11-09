class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def RLE(n):
            i = 0
            new_str = ""
            while (i < len(n)):
                curr_char = n[i]
                count = 1
                j = i + 1
                while(j < len(n) and n[j] == curr_char):
                    count += 1
                    j += 1
                
                new_str += (str(count) + curr_char)
                i = j
            #print("RLE of " + n + " is" + new_str)
            return new_str

        
        if(n == 1):
            return "1"

        return RLE(self.countAndSay(n - 1))
