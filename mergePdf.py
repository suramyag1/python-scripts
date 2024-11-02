from pypdf import PdfWriter
import glob
import os
import argparse
import sys

def parseArgs(args = None):

    parser = argparse.ArgumentParser(description='Merge multiple PDFs from a given directory.')
    parser.add_argument('-d', '--directory', help = 'Directory for PDFs files', required = True, default= None)
    parser.add_argument('-o', '--outfile', help = 'Output file name', default = 'updated.pdf', required = False, type = str)
    return parser.parse_args(args)

def mergePdfs(directory:str = None, outFile:str = 'updated.pdf'):
    directory = os.path.abspath(directory)
    print(directory)
    pdfs = glob.glob(directory + os.sep + '*.pdf')
    merger = PdfWriter()
    for pdf in pdfs:
        merger.append(pdf)

    merger.write(outFile)
    merger.close()

if __name__ == '__main__':
    val = parseArgs(sys.argv[1:])
    src = val.directory
    outfile = val.outfile
    mergePdfs(src, outfile)
