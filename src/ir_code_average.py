#!/usr/bin/env python

import sys
import os.path
import pandas as pd
import numpy as np

global DEBUG
DEBUG = False
DEBUG = True

def print_sysout(method):
    def printed(*args, **kw):
        result = method(*args, **kw)
        if DEBUG:
            print '%s' %  (result, )
        return result
    return printed


def read_data_file(file_name):
    df = pd.read_csv(file_name, skipinitialspace = True)
    v = df.values

    # skip first off and last on pulse
    v = v.flatten()[1:-1]

    # reshape into a matrix
    m = v.reshape(len(v) / 2, 2, order = 'C')
    df = pd.DataFrame(m)
    df.columns = ['on', 'off']
    return df


def read_data_files(file_args):
    dfs = [read_data_file(file_name) for file_name in file_args]
    return dfs


def average_ir_signal(dfs):
    dfc = pd.concat(dfs, axis=1)
    df = dfc.groupby(level=0, axis=1).mean()
    return df


def round_value(x, multiple):
    return round(x / multiple, 0) * multiple


def normalize_ir_value(df, multiple = 20.0):
    df = df.applymap(lambda x: round_value(x, multiple))
    return df[['on', 'off']]


def check_file_exists(file_name):
    return os.path.isfile(file_name)


def get_args(file_args):
    file_names = []
    for file_name in file_args:
        if not check_file_exists(file_name):
            print 'file does not exist: %s' % (file_name, )
        else:
            file_names.append(file_name)
    return file_names


@print_sysout
def make_arduino_code(df):
    on_commands = df['on'].apply(lambda x: 'pulseIR(%0.0f);' % (x, ))
    off_commands = df['off'].apply(lambda x: 'delayMicroseconds(%0.0f);' % (x, ))
    dfp = pd.DataFrame({'on': on_commands, 'off': off_commands})
    return dfp[['on', 'off']].to_string(header = False, index = False)


def main():
    args = sys.argv[1:]
    file_args = get_args(args)
    dfs = read_data_files(file_args)
    df = average_ir_signal(dfs)
    df = normalize_ir_value(df)
    make_arduino_code(df)


if __name__ == '__main__':
    main()
