from word_counter import source_to_counter
from word_statistics import get_word_statistics
import utilities.utils as utils
from counter.counter_utils import delete_counter, counter_exists


@utils.timeit
def test_url(url):
    source_to_counter(source=url, source_type='url')


@utils.timeit
def test_string(s):
    source_to_counter(source=s, source_type='string')


@utils.timeit
def test_file(file_path):
    source_to_counter(source=file_path, source_type='file')


if __name__ == '__main__':

    if counter_exists():
        delete_counter()

    test_file("texty.txt")
    test_url("http://www.textfiles.com/100/cDc-0200.txt")
    test_string("Me ME mE me-me- me2 2me me,me.me, .me. -me-")
    word = 'me'
    print(word, get_word_statistics(word))
