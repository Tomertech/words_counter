import utilities.utils as utils
from collections import Counter
import pickle
import urllib.request
import re
from typing import List


def create_counter(text: str) -> Counter:
    """
    :param text: a given text
    :return: Counter of the number of appearances for each word in the text
    """
    cleaned_text = clean_text(text)
    words_list = split_to_words(cleaned_text)
    words_counter = Counter(words_list)
    return words_counter


def save_counter_to_file(counter: Counter, file_name='counter'):
    """
    :param counter: a given counter
    :param file_name: the desired name of the counter file
    """
    # if counter.pkl already exits - unite them
    if counter_exists():
        old_counter = load_counter_from_file()
        counter += old_counter

    with open(file_name + '.pkl', 'wb') as file:
        pickle.dump(counter, file, protocol=pickle.HIGHEST_PROTOCOL)


def load_counter_from_file(file_name='counter') -> Counter:
    """
    :param file_name: counter's name
    :return: the counter from the saved file if it is exists, a new counter otherwise
    """
    if counter_exists():
        with open(file_name + '.pkl', 'rb') as file:
            counter = pickle.load(file)
            return counter

    else:
        return Counter()


def counter_exists(file_name='counter') -> bool:
    return utils.file_exists(file_name + '.pkl')


def delete_counter(file_name='counter'):
    """
    :param file_name: the counter file we want to delete in .pkl format
    :return: None
    """
    utils.delete_file(file_name + '.pkl')


def url_to_counter(url: str) -> Counter:
    """
    :param url: a url to the text source as string
    :return: a counter with cleaned up words as keys and occurrences as values
    """
    try:
        text = urllib.request.urlopen(url).read().decode("utf-8")
        counter = create_counter(text)
        save_counter_to_file(counter)
        return counter

    except:
        print('ERROR: bad url was given - insert valid urls only')


def string_to_counter(text: str) -> Counter:
    """
    :param text: a given text
    :return: a counter with cleaned up words as keys and occurrences as values
    """
    try:
        counter = create_counter(text)
        save_counter_to_file(counter)
        return counter

    except:
        print('ERROR: bad argument was given - insert strings only')


def text_file_to_counter(file_path: str) -> Counter:
    """
    :param file_path: a given file path the the text file
    :return: a counter with cleaned up words as keys and occurrences as values
    """
    try:
        with open(file_path) as file:
            counter = create_counter(file.read())
            save_counter_to_file(counter)
            return counter

    except:
        print('ERROR: bad file path was given, file not found - insert valid file paths only')


def clean_text(text: str) -> str:
    """
    :param text: un-cleaned text
    :return: cleaned text in lower case

    Only alphabet sequences ('a'-'z' or 'A'-'Z' and spaces) will count as valid chars in the cleaned text
    Any non-alphabet char will be cleaned up
    Any non-alphabet char will be considered as a separator between chars sequences (words)
    """
    cleaned = re.sub('[^a-z ]+', ' ', text.lower())
    return cleaned


def split_to_words(s: str) -> List[str]:
    """
    :param s:  the string we want to split
    :return: list of the words
    """
    return list(re.split('\W+', s))
