'''
awk-py.standalone 0.1.1 Canary
'''
import sys
import re
version = [0,1,1]
path = sys.argv[0]
encoding = 'utf-8'
if len(sys.argv) >= 2 and sys.argv[1] != 'utf-8':
    encoding = sys.argv[1]
file = open(path,'r')
source = file.read()
file.close()
del file
file = open(path,'w')
lines = source.split('\n')
options = sys.argv[2:]
def end(file,source):
    file.write(source)
    file.close()
def run(cmd,path,stdin):
    from subprocess import Popen
    redoInst = Popen([cmd,path]+args)
    return redoInst.communicate(stdin)
