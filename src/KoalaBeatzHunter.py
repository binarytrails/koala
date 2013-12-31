#!/usr/bin/python
from Controller import Controller
import sys, getopt

TMP_FOLDER = "../../tmp/"
HELP_MESSAGE = "test.py -o <outputfolder>"

def main(argv):
    #TODO write default location depending on OS
    output = TMP_FOLDER
    try:
        opts, args = getopt.getopt(argv, "hi:o:",["ofolder="])
        if args.__len__() != 0: pass
        
    except getopt.GetoptError: print HELP_MESSAGE, sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h': print HELP_MESSAGE, sys.exit()
        elif opt in ("-o", "--ofolder"): output = arg
    print output
    Controller(output)
    
if __name__ == "__main__":
    main(sys.argv[1:])