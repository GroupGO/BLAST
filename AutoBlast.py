#!/usr/bin/env python


"""
Author: Henry Ehlers
WUR_Number: 921013218060

A script designed to ...
    -input:
    -output:

In order to provide readable and understandable code, the right indentation margin has been
increased from 79 to 99 characters, which remains in line with Python-Style-Recommendation (
https://www.python.org/dev/peps/pep-0008/) .This allows for longer, more descriptive variable
and function names, as well as more extensive doc-strings.
"""


from CommandLineParser import *
import os
import re


def get_contents(path_text_file):
    """

    :param path_text_file:
    :return:
    """
    paths = []
    with open(path_text_file) as text_file:
        for line in text_file:
            line = line.strip()
            if line:
                paths.append(line)
    return paths


def run_blast(fasta_paths, genome_names, output_dir):
    """
    Method to run blast n on multiple databases using multiple fasta-queries and save their
    output to a desired directory.

    :param fasta_paths:
    :param genome_names:
    :return:
    """
    print('Running BLASTN.')
    current_path = os.getcwd()
    for fasta in fasta_paths:
        fasta_name = re.split(r'\.|/', fasta)[-2]
        print('\tQuery: %s.' % fasta_name)
        for genome in genome_names:
            genome_name = re.split(r'\.|/', genome)[-1]
            print('\t\tDatabase: %s' % genome_name)
            os.chdir(genome)
            output = '%s_%s.txt' % (genome_name, fasta_name)
            cmd = 'blastn -outfmt 6 -query %s -db %s > %s%s' \
                  % (fasta, genome_name, output_dir, output)
            execute_on_command_line(cmd)
    os.chdir(current_path)


def main():
    fasta_paths, genome_names, output_directory = \
        get_command_line_arguments(['fasta_paths.txt', 'genome_paths.txt',
                                    '~/project/groups/go/Data/Blast_Data/Blast_Results/'])
    assert os.path.exists(genome_names), 'Genome Paths file [%s] does not exist.' % genome_names
    assert os.path.exists(fasta_paths), 'Fasta Paths file [%s] does not exist.' % fasta_paths
    fasta_paths, genome_names = get_contents(fasta_paths), get_contents(genome_names)
    for path in fasta_paths:
        assert os.path.exists(path), '%s does not exist.' % path
    run_blast(fasta_paths, genome_names, output_directory)


if __name__ == '__main__':
    main()
