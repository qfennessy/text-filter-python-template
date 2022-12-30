import argparse
import sys

# create an ArgumentParser object
parser = argparse.ArgumentParser(description='Process some integers.')

# add a "-f" optional argument with a required value
parser.add_argument('-f', '--file', type=argparse.FileType('r'), help='input file')

# parse the command line arguments
args = parser.parse_args()

# check if the file argument was provided
if args.file:
    # read from the file
    input_text = args.file.read()
else:
    # read from stdin
    input_text = sys.stdin.read()

# process the input text
processed_text = input_text.upper()

# write the processed text to stdout
sys.stdout.write(processed_text)
