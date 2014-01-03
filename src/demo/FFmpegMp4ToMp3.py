#!/usr/bin/python
import subprocess
import re, select, os, time, fcntl, sys
 
#ffmpeg -i prentend\ its\ a\ video\ game.mp4  -f mp3 -ab 320000 -vn music.mp3
 
cmd = 'ffmpeg -i ../../tmp/prentend.mp4 -f mp3 -ab 320000 -vn ../../tmp/prentend.mp3'
 
args = cmd.split()
  
p = subprocess.Popen(args)

p = subprocess.Popen(args, stderr=subprocess.PIPE)
  
while True:
    chatter = p.stderr.read(1024)
    
    print("OUTPUT>>> " + chatter.rstrip())
        
    pipe = subprocess.Popen(
            cmd,
            stderr=subprocess.PIPE,
            close_fds=True
      )
    fcntl.fcntl(
          pipe.stderr.fileno(),
          fcntl.F_SETFL,
          fcntl.fcntl(pipe.stderr.fileno(), fcntl.F_GETFL) | os.O_NONBLOCK,
    )
    while True:
        readx = select.select([pipe.stderr.fileno()], [], [])[0]
        
        if readx:
            chunk = pipe.stderr.read()
         
            if not chunk:
                break
         
            result = re.search(r'stime=(?P<time>S+) ', chunk)
            elapsed_time = float(result.groupdict()['time'])
            print result
            print elapsed_time
            print result.groupdict()['size']
            
            #get .mp4 length in seconds
            #do estimation: 320Kbps/8*seconds will be close enough
            
     
            time.sleep(10)
    sys.exit()