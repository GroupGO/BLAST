#!/usr/bin/env python


"""
Author: Henry Ehlers
WUR_Number: 921013218060

A script designed to .build a blast database.
    -inputs:    [1] input_fasta_path
                [2] type of database
                [3] name of the database
                [4] path of output folder

In order to provide readable and understandable code, the right indentation margin has been
increased from 79 to 99 characters, which remains in line with Python-Style-Recommendation (
https://www.python.org/dev/peps/pep-0008/) .This allows for longer, more descriptive variable
and function names, as well as more extensive doc-strings.
"""


from CommandLineParser import *
import os


def build_database(input_fasta, db_type, database_name, out_path):
    """
    Method to build a blast database using makeblastdb.

    :param input_fasta: The path of the fasta file to be used, given as a string.
    :param db_type: The type of database, given as a string.
    :param database_name: The name of the database, given as a string.
    :param out_path: The path to the output folder, given as a string.
    :return exit_code: True/False depending on whether the database was built or not.
    """
    path_tests = ['', '', '']
    for index, extension in enumerate(['nhr', 'nin', 'nsq']):
        path_tests[index] = '%s/%s.%s' % (out_path, database_name, extension)
    if not all(os.path.exists(file_path) for file_path in path_tests):
        print('Database being built.')
        cmd = 'makeblastdb -in %s -dbtype %s -out %s' % (input_fasta, db_type, database_name)
        execute_on_command_line(cmd)
        return True
    else:
        print('Database already built.')
        return False


def move_database(database_name, out_path):
    """
    Method to create (if necessary) the specified output directory and move the newly created
    database to that directory.

    :param database_name: The name of the database, given as a string.
    :param out_path: The path of the desired output folder.
    """
    if not os.path.exists(out_path):
        print('Output directory %s being created.' % out_path)
        execute_on_command_line('mkdir %s' % out_path)
    print('Database %s being moved to %s' % (database_name, out_path))
    for extension in ['nhr', 'nin', 'nsq']:
        execute_on_command_line('mv %s.%s %s' % (database_name, extension, out_path))


def main():
    """
    Method to create a database and move it the desired output folder.
    """
    input_fasta, db_type, database_name, out_path = get_command_line_arguments(
        ['/local/data/BIF30806_2015_2/project/genomes/Catharanthus_roseus/cro_scaffolds.min_200bp'
         '.fasta', 'nucl', 'Catharanthus_roseus',
         '/local/data/BIF30806_2015_2/project/groups/go/Data/Blast_Data/Catharanthus_roseus'])
    assert os.path.exists(input_fasta), 'Input Fasta file does not exist.'
    if build_database(input_fasta, db_type, database_name, out_path):
        move_database(database_name, out_path)


if __name__ == '__main__':
    main()
