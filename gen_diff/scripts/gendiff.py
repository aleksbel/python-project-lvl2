#!/usr/bin/env python3


import argparse
import json


def generate_diff(path_to_file1, path_to_file2):
    before_json = json.load(open(path_to_file1))
    after_json = json.load(open(path_to_file2))
    keys_before_file = set(list(before_json.keys()))
    keys_after_file = set(list(after_json.keys()))
    keys_intersection_files = keys_before_file & keys_after_file
    keys_before_diff_after = keys_before_file - keys_after_file
    keys_after_diff_before = keys_after_file - keys_before_file
    comparison_result = {}
    for k in keys_before_diff_after:
        comparison_result['- ' + k] = before_json[k]
    for k in keys_after_diff_before:
        comparison_result['+ ' + k] = after_json[k]
    for k in keys_intersection_files:
        if before_json[k] == after_json[k]:
            comparison_result[k] = before_json[k]
        else:
            comparison_result['+ ' + k] = before_json[k]
            comparison_result['- ' + k] = after_json[k]
    comparison_result = str(comparison_result)
    return comparison_result


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
                        '-f',
                        '--format',
                        help='set format of output'
                        )
    args = parser.parse_args()
    path_to_file1 = args.first_file
    path_to_file2 = args.second_file
    diff = generate_diff(path_to_file1, path_to_file2)
    print(diff)


if __name__ == '__main__':
    main()
