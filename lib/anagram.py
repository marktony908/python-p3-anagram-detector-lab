# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        # Get sorted version of the original word
        sorted_word = ''.join(sorted(self.word))
        
        # Filter possible anagrams
        result = []
        for candidate in possible_anagrams:
            if ''.join(sorted(candidate)) == sorted_word and candidate != self.word:
                result.append(candidate)
                
        return result
