import glob
import os
import sys
import argparse
'''
Simple script to move python scripts from Python 2 to Python 3.
'''
#TODO: Find out why the \n gets converted to \n\n from the 2to3 module.

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def parseArgs(args = None):

    parser = argparse.ArgumentParser(description='Move scripts from Python 2 to 3. Takes all files in a \n project/directory and \
    uses the 2to3 module.')
    parser.add_argument('-d', '--directory', help = 'Directory for python files', required = True, default= None)
    parser.add_argument('-i', '--inplace', help = 'Do not keep a backup', default = 'false', required = False, type = str2bool)
    return parser.parse_args(args)

if __name__ == '__main__':
    val = parseArgs(sys.argv[1:])
    src = val.directory
    inplace = val.inplace
    files = glob.iglob(src + '/**/*.py', recursive = True)
    if not inplace:
        for f in files:
            os.system('2to3 -w {}'.format(f))
    else:
        for f in files:
            os.system('2to3 -wn {}'.format(f))

