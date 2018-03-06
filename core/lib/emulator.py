'''
awk-py.emulator 0.1.0 Canary
'''
import sys
path = sys.argv[1]
encoding = 'utf-8'
if len(sys.argv) >= 3 and sys.argv[2] != 'utf-8':
    encoding = sys.argv[2]
file = open(path,'r')
source = file.read()
file.close()
del file
file = open(path,'w')
lines = source.split('\n')
options = sys.argv[3:]
def end(file,source):
    file.write(source)
    file.close()
