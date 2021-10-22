from counter.counter_utils import load_counter_from_file


def get_word_statistics(word: str) -> int:
    """
    :param word: the word we want to get statistics about
    :return: number of times the word appeared so far

    Receives a word and returns the number of times the word appeared so far (in all previous calls)
    """

    counter = load_counter_from_file()
    return counter[word]
