import os, errno
from subprocess import Popen, PIPE

def executeShellCommand(cmd):
    p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    return out.rstrip(), err.rstrip(), p.returncode

def deleteFile(filename):
    try:
        os.remove(filename)
        return "Deleted: " + filename
    except OSError as e:
        # errno.ENOENT = no such file or directory
        if e.errno != errno.ENOENT:
            raise
        else:
            return "No such file: " + filename
        
def getNthIndex(data, word, nth):
    """
    data: where er search
    word: what we search
    nth:    occurence of the word
    """
    parts= data.split(word, nth + 1)
    if len(parts) <= nth + 1:
        return -1
    return len(data) - len(parts[-1]) - len(word)

def getFFmpegFileDurationInSeconds(filename):
    cmd = "ffmpeg -i "+ filename +" 2>&1 | grep 'Duration' | cut -d ' ' -f 4 | sed s/,//"
    time = executeShellCommand(cmd)[0]
    h = int(time[0:2])
    m = int(time[3:5])
    s = int(time[6:8])
    ms = int(time[9:11])
    ts = (h * 60 * 60) + (m * 60) + s + (ms/60)
    return ts

def estimateFFmpegMp4toMp3NewFileSizeInBytes(duration, kbps):
    """
    * Very close but not exact.
    duration: current file duration in seconds
    kbps: quality in kbps, ex: 320000
    Ex:
        estim.:    12,200,000
        real:      12,215,118
    """
    return ((kbps * duration) / 8)
