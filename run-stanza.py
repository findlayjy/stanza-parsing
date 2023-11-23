#!/usr/bin/env python3

import stanza
import sys
import pandas as pd
import argparse

# Define a dictionary holding language-specific configurations.
configurations = {
    'en': {'processors': 'tokenize,mwt,pos,lemma,depparse'},
    'fr': {'processors': 'tokenize,mwt,pos,lemma,depparse'},
    'de': {'processors': 'tokenize,mwt,pos,lemma,depparse'},
    'it': {'processors': 'tokenize,mwt,pos,lemma,depparse'},
    'nl': {'processors': 'tokenize,pos,lemma,depparse'}
}

# Add arguments for language and input text; use English as the default language if none is provided
argparser = argparse.ArgumentParser()
argparser.add_argument('-l', '--language', type=str, help='The language to use for the pipeline', default='en')
argparser.add_argument('-i', '--input', type=str, help='The text to be parsed')
argparser.add_argument('input_noflag', nargs='?', type=str, help='The text to be parsed')
args = argparser.parse_args()

# Determine the source of input
input_source = args.input or args.input_noflag

# Manually check if the text input argument is provided, else raise an error.
if input_source is None:
    argparser.error("No input provided. Please enter a text to parse, either directly, or using the -i or --input flag.")

# Choose the configuration based on language argument
language_config = configurations.get(args.language, configurations['en'])

nlp = stanza.Pipeline(args.language, **language_config, use_gpu=True, pos_batch_size=3000, logging_level='ERROR')

# parse the input
doc = nlp(input_source)
# convert the document to a list of dicts
for sentence in doc.sentences:
    # exclude start_char and end_char
    data = [{k: v for k, v in word.to_dict().items() if k not in ['start_char', 'end_char']} for word in sentence.words]
    # # include everything
    # data = [word.to_dict() for word in sentence.words]
# print it in a table using pandas
df = pd.DataFrame(data)
df = df.fillna("-")
print(df.to_string(index=False))
