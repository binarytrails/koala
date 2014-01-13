from threading import Thread
from time import sleep
import Queue
import uuid

import sys
sys.path.insert(0, '/home/koala/Git/KoalaBeatzHunter/src/app')
import Beat

"""
:Case
Prevent thread from starting, if first isnt finished.

:Logic
Download <-- Finished? (Conversion) & stop after waiting for too long.

:Implementation
sdownload --> Queue <-- sconvert (block if no updates, stop if timeout.)
"""

def sdownload(q):
    for i in range(1, 5):
        q.put(i)
        print "Downloaded " + str(25 * i) + "%"
        sleep(0.1)

def sconvert(q):
    while True:
        try:
            print q.get(timeout=1)
        except Queue.Empty:
            print "Finished no updates for 1 second."
            break

# q = Queue.Queue()

# dt = Thread(target = sdownload, args=[q])
# dt.start()

# st = Thread(target = sconvert, args=[q])
# st.start()

"""
:Case
Multiple downloadings and convertings

:Logic
Two threads running, waiting for new beat objects
that has all the data they need.
Threads communicates via objects that arrives in queues.

:Implementation
dThread(download) listens -> dq (download queue)
same for conversion

"""
dq = Queue.Queue()
cq = Queue.Queue()

def dThread():
    while True:
        print "Waiting for downloads tasks.."
        try:
            print "Got new dtask! " + str(dq.get().getId())
        except Queue.Empty:
            pass

def cThread():
    while True:
        print "Waiting for converts tasks.."
        try:
            print "Got new ctask! " + str(cq.get().getId())
        except Queue.Empty:
            pass

Thread(target = dThread, args=[]).start()
Thread(target = cThread, args=[]).start()

b = Beat.Beat("url@domain.com", "Title", "Album", "Artist", 3000)
b2 = Beat.Beat("url@domain.com", "Title", "Album", "Artist", 3000)

dq.put(b)
cq.put(b2)