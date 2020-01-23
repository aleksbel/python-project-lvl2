#!/usr/bin/env python3


import json
import yaml
from .parsers import arguments_parsing


def print_diff(*args):
    print('{')
    for dic in args:
        for key in dic:
            print('{}: {}'.format(key, dic[key]))
    print('}')


def generate_diff(*args):
    # If a call from the command line
    if not args:
        path_to_file1, path_to_file2 = arguments_parsing()
    # If a call with file paths
    else:
        path_to_file1 = args[0]
        path_to_file2 = args[1]
    # Open files
    before_file = open(path_to_file1)
    after_file = open(path_to_file2)
    # Defining a parser
    if path_to_file1.endswith('yml'):
        parser = yaml.full_load
    elif path_to_file1.endswith('json'):
        parser = json.load
    else:
        print('Unknown file extension')
    # Convert files to python objects
    before_json = parser(before_file)
    after_json = parser(after_file)
    # Convert keys to sets
    keys_before_file = set(list(before_json.keys()))
    keys_after_file = set(list(after_json.keys()))
    # Find the same keys
    keys_intersection_files = keys_before_file & keys_after_file
    # We find the keys of only the first set
    keys_before_diff_after = keys_before_file - keys_after_file
    # We find the keys of only the second set
    keys_after_diff_before = keys_after_file - keys_before_file
    # Create and populate a dictionary
    for k in keys_before_diff_after:
        for_print3 = {}
        for_print3['- ' + k] = before_json[k]
    for k in keys_after_diff_before:
        for_print4 = {}
        for_print4['+ ' + k] = after_json[k]
    for k in keys_intersection_files:
        # Values ​​are the same
        if before_json[k] == after_json[k]:
            for_print1 = {}
            for_print1['  ' + k] = before_json[k]
        # The values ​​are different
        else:
            for_print2 = {}
            for_print2['+ ' + k] = before_json[k]
            for_print2['- ' + k] = after_json[k]
    print_diff(for_print1, for_print2, for_print3, for_print4)
    # Combining dictionaries
    comparison_result = for_print1
    comparison_result.update(for_print2)
    comparison_result.update(for_print3)
    comparison_result.update(for_print4)
    # Convert to sring
    comparison_result = json.dumps(comparison_result)
    # print(comparison_result)
    return comparison_result


def main():
    generate_diff()


if __name__ == '__main__':
    main()
