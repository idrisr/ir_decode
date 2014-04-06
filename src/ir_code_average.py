#!/usr/bin/env python

import sys
import os.path

def print_sysout(method):
    def printed(*args, **kw):
        result = method(*args, **kw)
        print '%s' %  (result, )
        return result
    return printed


def get_data_files():
    pass


def read_data_file():
    pass


def parse_data_file():
    pass


def average_ir_signal():
    pass


def normalize_ir_signal():
    pass


def check_file_exists(file_name):
    return os.path.isfile(file_name)


@print_sysout
def get_args(file_args):
    file_names = []
    for file_name in file_args:
        if not check_file_exists(file_name):
            print 'file does not exist: %s' % (file_name, )
        else:
            file_names.append(file_name)

    return file_names

def main():
    args = get_args(sys.argv[1:])

if __name__ == '__main__':
    main()
