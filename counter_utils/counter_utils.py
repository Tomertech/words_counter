import os
import pickle
import re
import urllib.error
import urllib.request
from collections import Counter
from typing import List

counter_file_name = 'counter.pkl'


def word_counter(source: str, source_type: str):
    """
    :param source: text path (url, file path or string)
    :param source_type: the type of the source
    :return: None

    Receives a text input and counts the number of appearances for each word in the input and saves the counter_utils.
    """

    if source_type == 'url':
        url_to_counter(source)
    elif source_type == 'file':
        text_file_to_counter(source)
    elif source_type == 'string':
        string_to_counter(source)


def create_counter(text: str) -> Counter:
    """
    :param text: a given text
    :return: Counter of the number of appearances of each word in the text
    """
    cleaned_text = clean_text(text)
    words_list = split_to_words(cleaned_text)
    counter = Counter(words_list)
    delete_redundant_words(counter)
    return counter


def delete_redundant_words(counter: Counter):
    del counter['']
    del counter[' ']


def save_counter_to_file(counter: Counter):
    """
    :param counter: a given counter
    """
    # unite old a new counter
    old_counter = load_counter_from_file()
    if old_counter:
        counter += old_counter

    with open(counter_file_name, 'wb') as file:
        pickle.dump(counter, file, protocol=pickle.HIGHEST_PROTOCOL)


def delete_counter():
    """
    resetting the counter (by deleting it)
    """
    if counter_exists():
        os.remove(counter_file_name)


def load_counter_from_file() -> Counter:
    """
    :return: the counter from the saved file if it exists, a new counter otherwise
    """
    if counter_exists():
        with open(counter_file_name, 'rb') as file:
            counter = pickle.load(file)
            return counter

    else:
        return Counter()


def counter_exists() -> bool:
    return os.path.exists(counter_file_name)


def delete_counter():
    if counter_exists():
        os.remove(counter_file_name)


def url_to_counter(url: str) -> Counter:
    """
    :param url: a url to the text source as string
    :return: a counter with cleaned up words as keys and occurrences as values
    """
    text = urllib.request.urlopen(url).read().decode("utf-8")
    counter = create_counter(text)
    save_counter_to_file(counter)
    return counter


def string_to_counter(text: str) -> Counter:
    """
    :param text: a given text
    :return: a counter with cleaned up words as keys and occurrences as values
    """
    counter = create_counter(text)
    save_counter_to_file(counter)
    return counter


def text_file_to_counter(file_path: str) -> Counter:
    """
    :param file_path: a given file path the the text file
    :return: a counter with cleaned up words as keys and occurrences as values
    """
    with open(file_path) as file:
        counter = create_counter(file.read())
        save_counter_to_file(counter)
        return counter


def clean_text(text: str) -> str:
    """
    :param text: uncleaned text
    :return: cleaned text in lower case

    Only alphabet sequences ('a'-'z' or 'A'-'Z' and spaces) will count as valid chars in the cleaned text
    Any non-alphabet char will be cleaned up
    Any non-alphabet char will be considered as a separator between chars consecutive sequences (words)
    """
    cleaned = re.sub('[^a-z ]+', ' ', text.lower())
    return cleaned


def split_to_words(s: str) -> List[str]:
    """
    :param s:  the string we want to split
    :return: list of the words
    """
    return list(re.split('\W+', s))
