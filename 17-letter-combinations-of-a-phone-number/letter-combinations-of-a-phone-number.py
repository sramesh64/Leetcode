class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        curr = []
        num_to_char = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        def dfs(i):
            if(i >= len(digits)):
                res.append(''.join(curr))
                return
            num = int(digits[i])
            for char in num_to_char[num]:
                curr.append(char)
                dfs(i+1)
                curr.pop()
            return

        dfs(0)
        return res
            

