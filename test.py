print('i Start')
print('  test.py for CircleCI')
from core.lib.emulator import *
from sys import argv
print('i from core.lib.emulator import *')
# if source != open(sys.argv[1],'r').read():
#   print(source,open(sys.argv[1],'r').read())
#   exit(1)
# if file != open(sys.argv[1],'w'):
#   exit(2)
if path != sys.argv[1]:
  exit(3)
if options != sys.argv[2:]:
  exit(4)
source = 'test.py'
print('i Processing...')
end(file,source)
print('i end(file,source)')
if open(path,'r').read() != source:
  exit(5)
print('i Success!')
print('i End')
print('i exit(0)')
exit(0)
