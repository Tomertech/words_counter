from counter_utils.counter_utils import load_counter_from_file, word_counter, delete_counter
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
        delete_counter()
        test_string("Hi! My name is (what?), my name is (who?), my name's Slim Shady")
        counter = load_counter_from_file()
        self.assertTrue(counter["my"] == 3)
        self.assertTrue(counter["what"] == 1)
        self.assertTrue(counter["hello"] == 0)
        self.assertTrue(counter["("] == 0)
        delete_counter()

    def test_my_string(self):
        delete_counter()
        test_string("Me ME mE me-me- me2 2me me,me.me, .me. 2 -me- m#@e $#m$$e  %^m_*e5 &7m09e2  mmee meme")
        counter = load_counter_from_file()
        self.assertTrue(counter["me"] == 12)
        self.assertTrue(counter["m"] == 4)
        self.assertTrue(counter["e"] == 4)
        self.assertTrue(counter["mmee"] == 1)
        self.assertTrue(counter["meme"] == 1)
        self.assertTrue(counter["2"] == 0)
        delete_counter()

    def test_file(self):
        delete_counter()
        test_file("captmidn.txt")
        counter = load_counter_from_file()
        self.assertTrue(counter["the"] == 190)
        self.assertTrue(counter["i"] == 85)
        self.assertTrue(counter["captain"] == 22)
        self.assertTrue(counter["rebels"] == 1)
        self.assertTrue(counter["1"] == 0)  # appears 4 times in the given text
        delete_counter()

    def test_url(self):
        delete_counter()
        test_url("http://www.textfiles.com/100/hack11a.txt")
        counter = load_counter_from_file()
        self.assertTrue(counter["the"] == 6073)
        self.assertTrue(counter["and"] == 3171)
        self.assertTrue(counter["as"] == 671)
        self.assertTrue(counter["hackers"] == 248)
        self.assertTrue(counter["1993"] == 0)  # appears 17 times in the given text
        delete_counter()


if __name__ == '__main__':
    unittest.main()
