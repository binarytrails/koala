import re

"""
Get size for every line.
Funny fact: if we use this with FFmpeg, insead of new lines,
it will give us the '/r' carriage return. Make a bypass or it wont work.
"""

data = """
Press ctrl-c to stop encoding
size=     582kB time=14.89 bitrate= 320.1kbits/s    
size=    1223kB time=31.29 bitrate= 320.1kbits/s    
size=    1934kB time=49.50 bitrate= 320.0kbits/s    
size=    2646kB time=67.74 bitrate= 320.0kbits/s    
size=    3361kB time=86.05 bitrate= 320.0kbits/s    
size=    4073kB time=104.25 bitrate= 320.0kbits/s    
size=    4768kB time=122.04 bitrate= 320.0kbits/s    
size=    5482kB time=140.33 bitrate= 320.0kbits/s    
size=    6179kB time=158.17 bitrate= 320.0kbits/s    
size=    6884kB time=176.22 bitrate= 320.0kbits/s    
size=    7567kB time=193.70 bitrate= 320.0kbits/s    
size=    8321kB time=213.00 bitrate= 320.0kbits/s    
size=    9069kB time=232.15 bitrate= 320.0kbits/s    
size=    9810kB time=251.14 bitrate= 320.0kbits/s    
size=   10556kB time=270.24 bitrate= 320.0kbits/s    
size=   11296kB time=289.18 bitrate= 320.0kbits/s    
size=   11929kB time=305.37 bitrate= 320.0kbits/s    
video:0kB audio:11929kB global headers:0kB muxing overhead 0.002137%
"""
def extractFileSize(data):
    regex = re.compile(r'^size=([^kB\n]+)', re.MULTILINE)
    matches = [m.groups() for m in regex.finditer(data)]
    if matches is not None:
        res = []
        for m in matches:
            # get one match per line
            text =  str(m[0])
            # remove space
            text = re.sub(r'^[^0-9]*', '', text)
            # remove all white spaces
            #text = re.sub('[ ]+', '', text)
            res.append(text)
        return res
print extractFileSize(data)

def getNextNewFileSize(data, sline):
    regex = re.compile(r'^size=([^kB\n]+)', re.MULTILINE)
    matches = [m.groups() for m in regex.finditer(data)]
    if matches is not None:
        line = 0
        for m in matches:
            line += 1
            if line == sline + 1:
                # get one match per line
                text =  str(m[0])
                # remove space
                text = re.sub(r'^[^0-9]*', '', text)
                return text
                break
print getNextNewFileSize(data, 1)





