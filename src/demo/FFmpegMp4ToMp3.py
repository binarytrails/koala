#!/usr/bin/python

import src.app.custom.Utilities as utls

filename = "../../tmp/AwesomeKoalaBeat.mp4"
cmdi = "ffmpeg -i ../../tmp/AwesomeKoalaBeat.mp4 2>&1"
cmdf = "ffmpeg -i ../../tmp/AwesomeKoalaBeat.mp4 -f mp3 -ab 320000 -vn ../../tmp/converted.mp3"

print utls.getFileSizeFromLs(filename)

# get new mp3 estimated size
secs = utls.getFFmpegFileDurationInSeconds(filename)
efsize = utls.estimateFFmpegMp4toMp3NewFileSizeInBytes(secs, 320000)
print efsize

utls.convertMp4ToMp3("AwesomeKoalaBeat.mp4", "AwesomeKoalaBeat.mp3",
                "../../tmp/", 320000, utls.callbackPrint, efsize)
        
        