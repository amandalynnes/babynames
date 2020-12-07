#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration. Here's what the HTML looks like in the
baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 - Extract all the text from the file and print it
 - Find and extract the year and print it
 - Extract the names and rank numbers and print them
 - Get the names data into a dict and print it
 - Build the [year, 'name rank', ... ] list and print it
 - Fix main() to use the extracted_names list
"""

__author__ = "Amanda Simmons, Piero Madar, Tim La, Pete M."

import sys
import re
import argparse


def extract_names(filename):
    """
    Given a single file name for babyXXXX.html, returns a
    single list starting with the year string followed by
    the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ...]
    """
    year_and_names = []
    name_rank_dict = {}
    with open(filename, 'r') as f:
        read_file = f.read()
    year = re.search(r'Popularity\sin\s(\d\d\d\d)', read_file)
    year = year.group(1)
    # num = re.search(r'>(\d)+<', read_file)
    # extracts all names and ranks into a list of 3-tuples
    names_and_ranks = re.findall(
        r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', 
        read_file
        )
    
    # populate names and ranks into a dictionary
    for rank, male_name, female_name in names_and_ranks:
        if male_name not in name_rank_dict:
            name_rank_dict[male_name] = rank
        if female_name not in name_rank_dict:
            name_rank_dict[female_name] = rank
    pass
    # populate year followed by alphabetized names and ranks into final list

    # name_2 = re.search(r'<td>\d</td><td>([a-zA-Z]+)</td>', read_file)
    # num = num.group(1)
    # name_1_final = n_1.group(1)
    # name_2 = n_1.group(2)
    # num_name_1 = name_1_final + ' ' + num
    # num_name_2 = name_2 + ' ' + num
    # year_and_names.append(year + ', ' + num_name_1 + ', ' + num_name_2)
    # return year_and_names


def create_parser():
    """Create a command line parser object with 2 argument definitions."""
    parser = argparse.ArgumentParser(
        description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more
    # filenames. It will also expand wildcards just like the shell.
    # e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main(args):
    # Create a command line parser object with parsing rules
    parser = create_parser()
    # Run the parser to collect command line arguments into a
    # NAMESPACE called 'ns'
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    file_list = ns.files

    # option flag
    create_summary = ns.summaryfile

    for file in file_list:
        file_names = extract_names(file)
        print('\n'.join(file_names))     # I want this to be my else

    # For each filename, call `extract_names()` with that single file.
    # Format the resulting list as a vertical list (separated by newline \n).
    # Use the create_summary flag to decide whether to print the list
    # or to write the list to a summary file (e.g. `baby1990.html.summary`).

    # +++your code here+++


if __name__ == '__main__':
    main(sys.argv[1:])
