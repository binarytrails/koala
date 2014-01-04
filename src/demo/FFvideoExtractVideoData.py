#!/usr/bin/python
"""

* ffvideo
    > sudo aptitude install python-dev cython libavcodec-dev libavformat-dev libswscale-dev python-pip
    > pip install ffvideo
"""

from ffvideo import VideoStream
 
#ffmpeg -i prentend\ its\ a\ video\ game.mp4  -f mp3 -ab 320000 -vn music.mp3

mfile = '../../tmp/prentend.mp4'


def print_info(vs):
    print '-' * 20
    print "codec: %s" % vs.codec_name
    print "duration: %.2f" % vs.duration
    print "frame size: %dx%d" % (vs.frame_width, vs.frame_height)
    print "frame_mode: %s" % vs.frame_mode


vs = VideoStream(mfile)
print_info(vs)

vs = VideoStream(mfile)

print_info(vs)

frame = vs.get_frame_at_sec(2)
print frame.size

# PIL image, required installed PIL
frame.image().save('../../tmp/prentend_frame2sec.jpeg')

# numpy.ndarray, required installed numpy
print frame.ndarray().shape