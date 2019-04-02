import glob
import sys
import os
import fileinput
import argparse

def parseArgs(args = None):

    parser = argparse.ArgumentParser(description='Remove whitespaces from blank lines from all the files in a directory.\
     Also create a backup. Helps in the pre-commit hook.')
    parser.add_argument('-d', '--directory', help = 'Directory for python files', required = True, default= None)
    parser.add_argument('-b', '--backup', help = 'Backup file extension', required = False, default= '.bak')
    return parser.parse_args(args)

def stripLine(src, backup):
    files = glob.iglob(src + '/**/*.py', recursive = True)
    for line in fileinput.input(files = files, inplace = True, backup = backup):
            line = line.rstrip()
            print(line)


if __name__ == '__main__':
    val = parseArgs(sys.argv[1:])
    directory = val.directory
    backup = val.backup
    stripLine(directory, backup)
