from counter.counter_utils import url_to_counter, string_to_counter, text_file_to_counter, delete_counter


def insert_source(source: str, source_type: str):
    """
    :param source: text path (url, file path or string)
    :param source_type: the type of the source
    :return: None

    Receives a text input and counts the number of appearances for each word in the input.
    """

    if source_type == 'url':
        url_to_counter(source)

    elif source_type == 'string':
        string_to_counter(source)

    elif source_type == 'file':
        text_file_to_counter(source)


def reset_counter():
    """
    resetting the counter (deleting it)
    """
    delete_counter()


