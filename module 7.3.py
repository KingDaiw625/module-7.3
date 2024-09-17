class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding= 'utf-8') as a:
                b = a.read().lower()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    b = b.replace(i, '')
                b = b.split()
            all_words[name] = b
        return all_words

    def find(self, word):
        all_word = {}
        for a, b in self.get_all_words().items():
            if word.lower() in b:
                all_word[a] = b.index(word.lower()) + 1
        return  all_word

    def count(self, word):
        count2 = {}
        for a, b in self.get_all_words().items():
            count2[a] = b.count(word.lower())
        return count2

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
