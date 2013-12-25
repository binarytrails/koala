#!/usr/bin/python

import DownloaderController
import sys, getopt

helpMsg = "test.py -o <outputfolder>"

def main(argv):
    #TODO write default location depending on OS
    outputLocation = ''
    
    try:
        opts, args = getopt.getopt(argv, "hi:o:",["ofolder="])
        if args.__len__() != 0: pass
        
    except getopt.GetoptError: print helpMsg, sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h': print helpMsg, sys.exit()
        elif opt in ("-o", "--ofolder"): outputLocation = arg
    
    DownloaderController.DownloaderController(outputLocation)

if __name__ == "__main__":
    main(sys.argv[1:])