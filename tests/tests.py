from word_counter import insert_source
from word_statistics import get_word_statistics
import utilities.utils as utils
from counter.counter_utils import delete_counter, counter_exists


def test_url():
    # url = 'http://textfiles.com/adventure/aencounter.txt'
    url = 'hp://textfiles.com/adventure/aencounter.txt'
    insert_source(source=url, source_type='url')


def test_string():
    string = \
        "Answers: 1. The script initially writes the text specified in the command to the file. for(1,1,n) " \
                "executes the type command n times. And each time the type command appends the file content in dummy.txt" \
                "to the same file. So the size of the file doubles with each iteration. So if you decrease the number of" \
                "characters in the initial file, automatically the size of the final file will also be lesser. " \
                "2. As explained above, if you execute the for loop n times, the size of the file at the end will be " \
                "pow(2,n)*number of characters in the initial text."
    insert_source(source=string, source_type='string')


def test_file():
    file_path = 'C:/Users/tashuach/lotr.txt'
    # 'C:/Users/tashuach/lotr.txt'
    #  'C:/Users/tashuach/OneDrive - Technion/Carreer/Interview/Lemonade/word_api/lotr.txt'
    insert_source(source=file_path, source_type='file')


if __name__ == '__main__':

    if counter_exists():
        delete_counter()
    test_file()
    # test_url()
    # test_string()
    word = 'the'
    print(word, get_word_statistics(word, print_stats=False))
