import argparse
from gendiff import generate_diff



def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        usage='gendiff [-h] [-f FORMAT] first_file second_file',
        description='Compares two configuration files and shows a difference.'
    )
    
    parser.add_argument(
        '-f', 
        '--format',
        dest='format',
        metavar='FORMAT',
        default='stylish',  # ← УСТАНОВЛЕНО ПО УМОЛЧАНИЮ!
        help='set format of output (default: stylish)'
    )
    
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    
    args = parser.parse_args()
    
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
