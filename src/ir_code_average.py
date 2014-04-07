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


def str_to_int(s, delim = ','):
    i = s.split(delim)
    return [int(j.strip()) for j in i]


def str_list_to_int(l):
    l = [str_to_int(i) for i in l]
    return l


def make_dataframes(splits):
    return [make_dataframe(split) for split in splits]


def make_dataframe(split):
    df = pd.DataFrame(split)
    v = df.values

    # skip first off and last on pulse
    v = v.flatten()[1:-1]

    # reshape into a matrix
    m = v.reshape(len(v) / 2, 2, order = 'C')
    df = pd.DataFrame(m)
    df.columns = ['on', 'off']
    return df


def split_data_file(dir_file):
    handle = open(dir_file, 'r')
    header = 'OFF, ON'

    breaks = [0]

    # expects blank line between data blocks
    for i, line in enumerate(handle):
        if line.isspace():
            breaks.append(i)

    handle.seek(0)
    lines = [line.rstrip() for line in handle.readlines()]
    breaks.append(len(lines))

    splits = []

    for i in range(len(breaks) - 1):
        if i == 0:
            start = breaks[i] + 1
        else:
            start = breaks[i] + 2

        end = breaks[i + 1]
        splits.append((lines[start: end]))

    return splits


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


def get_file_arg(file_name):
    if not check_file_exists(file_name):
        print 'file does not exist: %s' % (file_name, )
        sys.exit(1)

    return file_name


@print_sysout
def make_arduino_code(df):
    on_commands = df['on'].apply(lambda x: 'pulseIR(%0.0f);' % (x, ))
    off_commands = df['off'].apply(lambda x: 'delayMicroseconds(%0.0f);' % (x, ))
    dfp = pd.DataFrame({'on': on_commands, 'off': off_commands})
    return dfp[['on', 'off']].to_string(header = False, index = False)


def main():
    args = sys.argv[1]
    file_args = get_file_arg(args)
    splits = split_data_file(file_args)
    splits = [str_list_to_int(split) for split in splits]
    dfs = make_dataframes(splits)
    df = average_ir_signal(dfs)
    df = normalize_ir_value(df)
    make_arduino_code(df)


if __name__ == '__main__':
    main()
