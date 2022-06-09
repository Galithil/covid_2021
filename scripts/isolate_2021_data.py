#! /usr/bin/env python3

import argparse

def main(args):
    import pdb;pdb.set_trace()
    with open(args.datafile, 'r') as df:
        with open(args.out, 'w+') as of:

            of.write(df.readline())
            for line in df:
                if '2021' in line.split(';')[2]:
                    of.write(line)


parser = argparse.ArgumentParser("Isolate 2021 data from a gouv.fr dataset")

parser.add_argument('datafile', type=str, help="file path")
parser.add_argument('--out', '-o', default = 'data_2021.csv', type=str, help="path to write to")

args = parser.parse_args()

main(args)

