#!/usr/bin/python

from src.custom import Utilities
import subprocess, re

def getProgressPercentageFromBytes(size, fsize):
    """
    size:  current file size
    fsize: final file size
    """
    return size / fsize * 100

def callbackPrint(data):
    print data

def extractFFmpegFileSize(data):
    """
    Attention to carriage returns '/r' or in nano editor '^M'
    Function only extract 1 per line 'm[0] in matches'
    """
    regex = re.compile(r'^size=([^kB\n]+)', re.MULTILINE)
    matches = [m.groups() for m in regex.finditer(data)]
    if matches is not None:
        res = []
        for m in matches:
            text =  str(m[0])
            text = re.sub(r'^[^0-9]*', '', text)
            res.append(text)
        return res

def convertMp4ToMp3(mp4f, mp3f, odir, kbps, callback=None, efsize=None):
    """
    mp4f:     mp4 file
    mp3f:     mp3 file
    odir:     output directory
    kbps:     quality in kbps, ex: 320000
    callback: callback() to recieve progress
    efsize:   estimated file size, if there is will callback() with %
    Important:
    communicate() blocks until the child process returns, so the rest of the lines 
    in your loop will only get executed after the child process has finished running. 
    Reading from stderr will block too, unless you read character by character like here.
    """
    cmdf = "ffmpeg -i "+ odir+mp4f +" -f mp3 -ab "+ str(kbps) +" -vn "+ odir+mp3f
    lineAfterCarriage = ''
    
    print Utilities.deleteFile(odir + mp3f)
    
    child = subprocess.Popen(cmdf, shell=True, stderr=subprocess.PIPE)
    
    while True:
        char = child.stderr.read(1)
        if char == '' and child.poll() != None:
            break
        if char != '':
            # simple print to console
#             sys.stdout.write(char)
#             sys.stdout.flush()
            lineAfterCarriage += char
            if char == '\r':
                if callback:
                    size = int(extractFFmpegFileSize(lineAfterCarriage)[0])
                    if efsize:
                        size = getProgressPercentageFromBytes(efsize, size)
                    callback(size)
                lineAfterCarriage = ''

cmdi = "ffmpeg -i ../../tmp/AwesomeKoalaBeat.mp4 2>&1"
cmdf = "ffmpeg -i ../../tmp/AwesomeKoalaBeat.mp4 -f mp3 -ab 320000 -vn ../../tmp/converted.mp3"

# to write all the bellow data that prints to a file
#sys.stdout = open('data', 'w')

# get file size from ls -l
odir = "../../tmp/"
mp4f = "AwesomeKoalaBeat.mp4"
res = Utilities.executeShellCommand("ls -l "+ odir+mp4f)
out = str(res[0])
idxf = Utilities.getNthIndex(out, ' ', 3) + 1
idxl = Utilities.getNthIndex(out, ' ', 4)
fsize = out[idxf:idxl]

# get new mp3 estimated size
secs = Utilities.getFFmpegFileDurationInSeconds(odir+mp4f)
efsize = Utilities.estimateFFmpegMp4toMp3NewFileSizeInBytes(secs, 320000)
print efsize

convertMp4ToMp3("AwesomeKoalaBeat.mp4", "AwesomeKoalaBeat.mp3",
                "../../tmp/", 320000, callbackPrint, efsize)
        
        