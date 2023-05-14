#! python3
# @Author: Jaedan Willis
# @Company: Official Grasp Technology

import sys
import string
import random
import argparse
import itertools
try:
    import pyperclip
except ImportError as e:
    raise ImportError(str(e))


class OGTKeyGenertor:

    @classmethod
    def generate(cls, length: int):
        if length <= 0:
            raise ValueError('length should be grater than 0.')

        key = ''
        lst = list(itertools.repeat(0, length))

        for _ in lst:
            digits = random.choice(string.digits)
            lower = random.choice(string.ascii_lowercase)
            upper = random.choice(string.ascii_uppercase)
            symbols = random.choice(string.punctuation)
            if len(key) < int(length):
                key += random.choice([lower, digits, symbols, upper])
            else:
                break
        pyperclip.copy(key)
        print(
            f'\nKey generated ({key}) with ({len(key)}) characters and is copied to clip board.\n')
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--length', help='How long you want the generated key to be',
                        type=int,  required=True)
    args = parser.parse_args()

    if args.length:
        OGTKeyGenertor.generate(length=args.length)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
