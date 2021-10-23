from counter_utils.counter_utils import load_counter_from_file


def word_statistics(word: str) -> int:
    """
    Receives a word and returns the number of times the word appeared so far (in all previous calls)
    """
    if not isinstance(word, str):
        print("ERROR: word must be a string")
        return 0

    counter = load_counter_from_file()
    return counter[word]
