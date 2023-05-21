import sys
import os
import argparse
from PyPDF2 import PdfMerger

parser = argparse.ArgumentParser(description="Merge individual PDF files into one file")

parser.add_argument("-h",required=False)
parser.add_argument('-c',required=False, help="Uses current directory to look for PDF files")
parser.add_argument('-d',type=str,metavar="C:\\Users\\admin\\Desktop\\pdfs",help='Full directory path to individual PDFs')
parser.add_argument('-f',type=str,metavar="C:\\Users\\admin\\Desktop\\pdfs",help='Full file path for final PDF')

# try:
#     errMsg = ''
#     if sys.argv[1] == '' or sys.argv[2] == '':
        
# except IndexError:
#     print('Please provide directory path and final file path for merge')

# else:

# argv = sys.argv[1:]

# try:
#     opts, args = getopt.getopt(argv,"c:d:f:h:")
# except Exception as e:
#     print('No options passed')
for opt, arg in opts:
    if opt in ['-h']:
        print('''
        Merges PDF pages together
        -h help -> Help
        -c . -> run in current directory
        -d[directorypath] -> directory path that contains pdfs
        -f[filepath] -> file path of output file
        ''')
        sys.exit(0)
    elif opt in ["-c"]:
        pdfDir = os.getcwd()
    elif opt in ['-d']:
        if '/' in arg:
            arg = arg.replace('/','\\')
        if os.path.isdir(arg):
            pdfDir = arg
        else:
            print('PDF Directory path does not exist.')
            sys.exit(1)
    elif opt in ['-f']:
        if "/" in arg:
            arg = arg.replace('/','\\')
        finalFilePath = arg

merger = PdfMerger()
try:
    for f in os.listdir(pdfDir):
        merger.append(f"{pdfDir}\\{f}")
    merger.write(finalFilePath)
    merger.close()
    # for f in os.listdir(sys.argv[1]):
    #     merger.append(f"{sys.argv[1]}\\{f}")
    # merger.write(f"{os.environ['USERPROFILE']}\\Desktop\\MergedPdf.pdf")
    # merger.close()
    print(f'file has been written')
except IndexError:
    print('Please provide directory with pdf files')
    sys.exit(1)
except Exception as e:
    print(str(e))
    sys.exit(1)