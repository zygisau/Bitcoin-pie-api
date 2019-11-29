import sys

from src.extractor import Extractor

if __name__ == '__main__':
    # noinspection SpellCheckingInspection
    switcher = {
        'calcfee': lambda: Extractor.calculate_fee(sys.argv[2]),
        'validateblock': lambda: Extractor.validate_block(sys.argv[2])
    }
    print(switcher.get(sys.argv[1], f'Unknown argument {sys.argv[1]}')())
