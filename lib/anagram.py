# your code goes here!
from collections import Counter

class Anagram :
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        word_counter = Counter(self.word)
        return [word for word in word_list if Counter(word) == word_counter]

listen = Anagram("listen")
print(listen.match(['enlist', 'google', 'inlets', 'banana']))