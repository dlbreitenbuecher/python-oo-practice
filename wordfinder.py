from random import choice 
class WordFinder:
    """Word Finder: finds random words from a dictionary.

     >>> word_finder = WordFinder("/Users/shweta/Desktop/words.txt")
     3 words read

     >>> word_finder.get_random_word
     'ugly'

     """
    
    def __init__(self, file_path):
        """Reads a file and invokes create_word_list and prints the length of word_list """
        self.file = open(file_path)
        self.word_list = self.create_word_list(self.file)
        print(f"{len(self.word_list)} words read")

    
    def create_word_list(self, file):
        """Reads file line by line and trims any new line chars if present. Puts each word in a word_list and return the list"""
        word_list = []
        for line in self.file :
            word_list.append(line.strip())
        return  word_list

    def get_random_word(self):
        """Returns one random word from the word_list"""
        return choice(self.word_list)
