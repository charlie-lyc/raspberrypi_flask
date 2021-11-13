from flask import Flask


app = Flask(__name__)

@app.route('/')
def helloworld():
    return 'Hello World!`'


if __name__ == '__main__':
    app.run(host='0.0.0.0')


############################################
### Error 'Port(Address) already in use' ### 
############################################
## Check PID of process or port
# $ ps -ef | grep <filename>
## OR
# $ netstat -nlpt
## Kill process
# $ sudo kill <pid>
############################################

###### Using Process ######

## Run
# $ python 08_process.py

## Open another terminal check foreground process
# $ ps
## Check foreground process in detail
# $ ps -f
## Check background process in detail
# $ ps -ef

## Check only process.py
# $ ps -ef | grep process.py
# UID        PID  PPID  C STIME TTY          TIME CMD
# pi        2093  1756  0 17:08 pts/0    00:00:00 python 08_process.py
# pi        2142  2097  0 17:14 pts/1    00:00:00 grep --color=auto process.py

## Kill process in PID
# $ sudo kill 2093

## Check process
# $ ps -ef | grep process.py
# UID        PID  PPID  C STIME TTY          TIME CMD
# pi        2158  2097  0 17:16 pts/1    00:00:00 grep --color=auto process.py

## Check in another terminal
# => Terminated 

###### Using Port ######

## Run
# $ python 08_process.py

## Check port
# $ netstat -nlpt
# Active Internet connections (only servers)
# Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
# tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
# tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      -                   
# tcp        0      0 127.0.0.1:43163         0.0.0.0:*               LISTEN      1879/code           
# tcp        0      0 0.0.0.0:5000            0.0.0.0:*               LISTEN      2196/python         
# tcp        0      0 0.0.0.0:5900            0.0.0.0:*               LISTEN      -                   
# tcp6       0      0 :::22                   :::*                    LISTEN      -                   
# tcp6       0      0 ::1:631                 :::*                   

## Kill process in PID
# $ sudo kill 2196

## Check port
# $ netstat -nlpt
# Active Internet connections (only servers)
# Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
# tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
# tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      -                   
# tcp        0      0 127.0.0.1:43163         0.0.0.0:*               LISTEN      1879/code           
# tcp        0      0 0.0.0.0:5900            0.0.0.0:*               LISTEN      -                   
# tcp6       0      0 :::22                   :::*                    LISTEN      -                   
# tcp6       0      0 ::1:631                 :::*                    LISTEN      -                   
# tcp6       0      0 :::5900                 :::*                    LISTEN      -      

## Check in another terminal
# => Terminated 