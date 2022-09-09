from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        # pass
        self.head = None


    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED
        for word in words_frequencies:
            self.add_word_frequency(word)


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """

        # TO BE IMPLEMENTED
        item = self.head
        while item is not None:
            if item.word_frequency[0] == word:
                return item.word_frequency[1]
            item = item.next
        return 0
            



    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        # TO BE IMPLEMENTED
        word_frq_tuple = (word_frequency.word, word_frequency.frequency)
        if self.head is None:
            self.head = ListNode(word_frq_tuple)
            return True
        ll_item = self.head   
        while True:
            if ll_item.word_frequency[0] == word_frequency.word:
                return False
            if ll_item.next is None:
                break
            ll_item = ll_item.next
        ll_item.next = ListNode(word_frq_tuple)
        return True



    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        temp = self.head
        if temp is not None:
            if temp.word_frequency[0] == word:
                self.head = temp.next
                temp = None
                return True
        while temp is not None:
            if temp.word_frequency[0] == word:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return False
        prev.next = temp.next
        temp = None
        return True


    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        prefix_word_length = len(prefix_word)
        most_frq_words = []
        ll_item = self.head
        while ll_item is not None:
            word, word_frq = ll_item.word_frequency[0], ll_item.word_frequency[1]
            if word.startswith(prefix_word):
                most_frq_words.append((word, word_frq))
                most_frq_words.sort(key=lambda word_frq_tuple: word_frq_tuple[1], reverse=True)
            ll_item = ll_item.next
        most_frq_words = most_frq_words[:3]
        return_lst = []
        for word, word_frq in most_frq_words:
            return_lst.append(WordFrequency(word, word_frq))
        return return_lst





