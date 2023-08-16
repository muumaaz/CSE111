#2
class SentenceAnalyzer:
    def __init__(self, sentence = None):
        self.sentence = sentence

    def set_sentence(self, sentence):
        self.sentence = sentence

    def get_word_count(self, length = None):
        words = self.sentence.split()

        if length is None:
            count = len(words)
            print(f"Number of words in sentence: {count}")
        else:
            filtered_words = [word for word in words if len(word) == length]
            print(f"Number of words with {length} characters in the sentence: {len(filtered_words)}")


analyzer1 = SentenceAnalyzer()


analyzer1.set_sentence("That's an easy one")
print("1--------------------------")
analyzer1.get_word_count()
print("2--------------------------")
analyzer2 = SentenceAnalyzer("Like I said it's easy")


print("3--------------------------")
analyzer2.get_word_count()


print("4--------------------------")
analyzer2.get_word_count(4)
print("5--------------------------")
analyzer1.get_word_count(5)