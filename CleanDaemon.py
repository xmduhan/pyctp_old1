# -*- coding: utf-8 -*-
import os
import sys
import signal
from time import sleep

def isProcessRunning(pid):
    '''
    检查进程是在运行
    '''
    try:
        os.kill(int(pid), 0)
        return True
    except OSError:
        return False


def kill(pid):
    '''
    杀死进程
    '''
    os.kill(int(pid), signal.SIGQUIT)


def main():
    '''
    守护进程,主要用于检查父进程是否还在,否则将清理通讯进程
    '''
    # 检查参数使用是否正确
    print sys.argv
    if len(sys.argv) != 2:
        print u'请使用:python CleanDaemon.py pid 来启动程序'
        return

    # 检查指定的进程是否存在
    pid = sys.argv[1]
    print 'isProcessRunning(pid)=',isProcessRunning(pid)
    if isProcessRunning(pid) == False :
        print u'指定的进程(pid=%s)并没有在运行' % pid
        return

    print u'cleanDaemon():start'
    ppid = os.getppid()
    while ppid != 1 :
        sleep(1)
        ppid = os.getppid()
    print u'cleanDaemon():main process stop'

    # 这行到这里说明主进程终止(ppid=1),需要对通讯进程进行清理
    kill(pid)
    print u'cleanDaemon():clean'


if __name__ == '__main__':
    main()
    #os.kill(6003,0)
