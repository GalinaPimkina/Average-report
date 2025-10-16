import argparse


def get_one_type(string):
    return '_'.join([word for word in string.split('-')])


parser = argparse.ArgumentParser(description='Get list of files names')
parser.add_argument(
    '--files',
    nargs='+',
    type=str,
    help='provide a file name',
    required=True,
)
parser.add_argument(
    '--report',
    type=get_one_type,
    help='provide a report name',
    required=True,
)

data = parser.parse_args()