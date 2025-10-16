import argparse


parser = argparse.ArgumentParser(description='Get list of files names')
parser.add_argument(
    '--files',
    nargs='+',
    type=str,
    help='provide a file name',
    required=True,
)