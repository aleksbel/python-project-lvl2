#!/usr/bin/env python3


import argparse
import yaml
import json


def arguments_parsing():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
                        '-f',
                        '--format',
                        help='set format of output'
                        )
    args = parser.parse_args()
    return args.first_file, args.second_file


def file_parsing(path_to_file1, path_to_file2):
    if path_to_file1.endswith('yml'):
        parser = yaml.full_load
    elif path_to_file1.endswith('json'):
        parser = json.load
    else:
        print('Unknown file extension')
    return parser(open(path_to_file1)), parser(open(path_to_file2))
