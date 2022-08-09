from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import bisect


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ArrayDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.array = []


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

        for my_word, word_frq in self.array:
            if my_word == word:
                return word_frq
        return 0

        # try:
        #     index_of_word = [word_frq[0] for word_frq in self.array].index(word)
        #     return self.array[index_of_word][1]
        # except ValueError:
        #     return 0


    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED

        word, word_frq = word_frequency.word, word_frequency.frequency

        word_frq_tuple = (word, word_frq)

        if len(self.array) == 0:
            self.array.append(word_frq_tuple)
            return True
        else:
            for index in range(len(self.array)):
                # if word is in array
                if self.array[index][0] == word:
                    return False
                else:
                    self.array.append(word_frq_tuple)
                    return True


    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # find the position of 'word' in the list, if exists, will be at idx-1
        # TO BE IMPLEMENTED

        for index, word_frq_tuple in enumerate(self.array):
            if word_frq_tuple[0] == word:
                self.array.pop(index)
                return True
        return False


    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        
        most_frq_words = []
        for word, word_frq in self.array:
            if word[0:len(prefix_word)] == prefix_word:
                most_frq_words.append((word, word_frq))
                # sorting most_frq_words list using the frq of each word in reverse order
                most_frq_words.sort(key=lambda word_frq_tuple: word_frq_tuple[1], reverse=True)

        most_frq_words = most_frq_words[:3]

        return_lst = []
        for word, word_frq in most_frq_words:
            return_lst.append(WordFrequency(word, word_frq))

        return return_lst
