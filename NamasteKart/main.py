import os
import csv
import datetime as dt


def generate_file_path():
    '''
        This will generate your file directory by assuming it to be in format yyyymmdd
    :return:
        str - File directory based on current date.
    '''
    source_prefix = 'incoming_files'
    file_dir = dt.date.today().strftime('%Y%m%d')
    return '/'.join([source_prefix, file_dir])

def read_files(loc):
    '''
        This function reads all the files and their data into OrderedDict
    :param loc: Directory location where all data is residing.
    :return:
        It returns dict of file: data_in_the_file
    '''
    files = {i: '' for i in os.listdir(loc)}
    for file in files.keys():
        print(f'Reading {file}')
        data = []
        with open('/'.join([loc, file])) as csv_file:
             for rows in csv.DictReader(csv_file):
                 data.append(rows)
        files[file] = data
        return files

def display_files(files):
    '''
    This will display all the data of all the files in that are in params.
    :param files:
    '''
    for file, data in files.items():
        print(f'We are reading {file}')
        for cols in data[0].keys():
            print('{: <15}'.format(cols), end = '')
        print()
        for row in data:
            for record in row.values():
                print('{: <15}'.format(record), end = '')
            print()

if __name__ == '__main__':
    file_loc = generate_file_path()
    files = read_files(file_loc)
    display_files(files)
