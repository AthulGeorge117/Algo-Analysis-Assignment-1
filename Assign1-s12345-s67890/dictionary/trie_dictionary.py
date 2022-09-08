from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

# in order to test run one of these commands the the cl
# python dictionary_file_based.py trie sampleDataToy.txt testToy.in testToy.out
# python3 dictionary_file_based.py trie sampleDataToy.txt testToy.in testToy.out

# Class representing a node in the Trie
class TrieNode:

    def __init__(self, letter=None, frequency=None, is_last=False):
        self.letter = letter            # letter stored at this node
        self.frequency = frequency      # frequency of the word if this letter is the end of a word
        self.is_last = is_last          # True if this letter is the end of a word
        self.children: dict[str, TrieNode] = {}     # a hashtable containing children nodes, key = letter, value = child node


class TrieDictionary(BaseDictionary):

    def __init__(self):
        self.root = TrieNode("")

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        for word in words_frequencies:
            self.add_word_frequency(word)



    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return 0

        if node.is_last:
            return node.frequency

        return 0


    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        node = self.root
        for char in word_frequency.word :
            if char in node.children:
                node = node.children[char]

            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        
        if node.is_last:
            return False

        node.is_last = True
        node.frequency = word_frequency.frequency
        return True


    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        if node.is_last == False:
            return False
        node.is_last = False
        node.frequency = None
        return True


    def traverse(self , node , prefix) :
        """Depth-first traversal of the trie
        
        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if node.is_last:
            self.wordslist.append(WordFrequency(prefix + node.letter , node.frequency))
        for each in node.children.values() :
            self.traverse(each , prefix + node.letter)



    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        node = self.root
        self.wordslist = []
        for char in prefix_word:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        self.traverse(node, prefix_word[:-1])
        self.wordslist.sort(reverse=True, key=lambda y: y.frequency)
        return self.wordslist[:3]