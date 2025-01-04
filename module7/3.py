def sep_punctuation(words):
    punctuation = ",.=!?;:-"
    result = []

    for word in words.split():
        w = word.lower()
        for sym in punctuation:
            if sym in word:
                w = word.replace(sym, '')
        result.append(w)

    return result


class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):

        all_words = {}

        for filename in self.file_names:
            with open(filename, 'r', encoding='utf-8') as file:
                words_in_file = []

                for line in file:
                    words_in_file.extend(sep_punctuation(line))

                all_words[filename] = words_in_file

        return all_words

    def find(self, word):
        find_word = {}
        word = word.lower()

        for k, v in self.get_all_words().items():
            find_word[k] = v.index(word) + 1

        return find_word

    def count(self, word):
        count_word = {}
        word = word.lower()

        for k, v in self.get_all_words().items():
            count_word[k] = v.count(word)

        return count_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
