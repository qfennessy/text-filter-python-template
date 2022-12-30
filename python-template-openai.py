import argparse
import configparser
import os
import sys
import requests
import openai
import base64

# create the parser
parser = argparse.ArgumentParser(description='Generate an image with DALL-E')

# add the --input and --url arguments
parser.add_argument('--input', type=argparse.FileType('r'),
                    help='input file (defaults to stdin)')
parser.add_argument('--url', type=str, help='input URL')

# parse the arguments
args = parser.parse_args()

# try to read the API key from the .openai-api file
config = configparser.ConfigParser()
config.read(os.path.expanduser('~/.openai-api'))

# check if the --url argument was provided
if args.url:
    # read the input from the URL
    input_text = requests.get(args.url).text
else:
    # get the input file (either from the --input argument or stdin)
    input_file = args.input or sys.stdin

    # read the input
    input_text = input_file.read()

openai.api_key = config['openai']['api_key']
print ("API KEY ", openai.api_key)

response = openai.Image.create(prompt=input_text, model='image-alpha-001')
image_url = response['data'][0]['url']
print ("URL = ", image_url)