import argparse
from counter_utils.counter_utils import word_counter, delete_counter, load_counter_from_file

# this is a Command Line Interface

parser = argparse.ArgumentParser('word counter and statistics.', add_help=False)

parser.add_argument('--service', choices=['counter', 'c', 'statistics', 's', 'reset', 'r'], type=str,
                    required=False,
                    help='insert a text source ("counter" or "c"), get word statistics '
                         '("statistics" or "s") or reset the counter ("reset" or "r")')
parser.add_argument('--source', type=str, required=False, help='The source of the text file - url, file path or string')
parser.add_argument('--type', choices=['url', 'file', 'string'], type=str, required=False,
                    help='type of the source - url, file or string')
parser.add_argument('--word', type=str, required=False,
                    help='the word we want to see how many times it appeared so far')

args = parser.parse_args()

if args.service in ['counter', 'c']:
    print('Got it!')
    word_counter(args.source, args.type)

elif args.service in ['statistics', 's']:
    counter = load_counter_from_file()
    word = args.word.lower()
    print(f'The word "{word}" appeared so far {counter[word]} times')

elif args.service in ['reset', 'r']:
    delete_counter()
    print('Counter was reset')

