class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_dict = dict()
        for char in chars:
            if(char not in char_dict):
                char_dict[char] = 0
            char_dict[char] += 1


        count = 0
        for word in words:
            word_dict = dict()
            good = True
            for char in word:
                if(char not in word_dict):
                    word_dict[char] = 0
                word_dict[char] += 1
                if(char not in char_dict or word_dict[char] > char_dict[char]):
                    good = False
                    break
            if(good == True):

                count += len(word)
                
        return count


