import os
from counter_utils.counter_utils import url_to_counter, string_to_counter, text_file_to_counter, counter_exists, counter_file_name


def word_counter(source: str, source_type: str):
    """
    :param source: text path (url, file path or string)
    :param source_type: the type of the source
    :return: None

    Receives a text input and counts the number of appearances for each word in the input and saves the counter_utils.
    """
    if not isinstance(source, str):
        print("ERROR: source must be a string")
        return

    if source_type == 'url':
        url_to_counter(source)
    elif source_type == 'file':
        text_file_to_counter(source)
    elif source_type == 'string':
        string_to_counter(source)
    else:
        print("ERROR: source type must be one of the following: 'url', 'file' or 'string'")


def reset_counter():
    """
    resetting the counter (by deleting it)
    """
    if counter_exists():
        os.remove(counter_file_name)


