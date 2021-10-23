import argparse
from word_counter import word_counter, reset_counter
from word_statistics import word_statistics

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
    print('Got it, now processing...')
    word_counter(args.source, args.type)
    print('Done')

elif args.service in ['statistics', 's']:
    count = word_statistics(args.word)
    print(f'The word "{args.word}" appeared so far {count} times')

elif args.service in ['reset', 'r']:
    reset_counter()
    print('counter was reset')

