from word_counter import word_counter, reset_counter
from word_statistics import word_statistics
from utils.timer import timeit
import unittest


@timeit
def test_url(url):
    word_counter(source=url, source_type='url')


@timeit
def test_string(s):
    word_counter(source=s, source_type='string')


@timeit
def test_file(file_path):
    word_counter(source=file_path, source_type='file')


class Tests(unittest.TestCase):

    def test_given_string_example(self):
        reset_counter()
        test_string("Hi! My name is (what?), my name is (who?), my name's Slim Shady")
        self.assertTrue(word_statistics("my") == 3)
        self.assertTrue(word_statistics("what") == 1)
        self.assertTrue(word_statistics("hello") == 0)
        self.assertTrue(word_statistics("(") == 0)
        reset_counter()

    def test_my_string(self):
        reset_counter()
        test_string("Me ME mE me-me- me2 2me me,me.me, .me. 2 -me- m#@e $#m$$e  %^m_*e5 &7m09e2  mmee meme")
        self.assertTrue(word_statistics("me") == 12)
        self.assertTrue(word_statistics("m") == 4)
        self.assertTrue(word_statistics("e") == 4)
        self.assertTrue(word_statistics("mmee") == 1)
        self.assertTrue(word_statistics("meme") == 1)
        self.assertTrue(word_statistics("2") == 0)
        reset_counter()

    def test_file(self):
        reset_counter()
        test_file("captmidn.txt")
        self.assertTrue(word_statistics("the") == 190)
        self.assertTrue(word_statistics("i") == 85)
        self.assertTrue(word_statistics("captain") == 22)
        self.assertTrue(word_statistics("rebels") == 1)
        self.assertTrue(word_statistics("1") == 0)  # appears 4 times in the given text
        reset_counter()

    def test_url(self):
        reset_counter()
        test_url("http://www.textfiles.com/100/hack11a.txt")
        self.assertTrue(word_statistics("the") == 6073)
        self.assertTrue(word_statistics("and") == 3171)
        self.assertTrue(word_statistics("as") == 671)
        self.assertTrue(word_statistics("hackers") == 248)
        self.assertTrue(word_statistics("1993") == 0)  # appears 17 times in the given text
        reset_counter()


if __name__ == '__main__':
    unittest.main()
