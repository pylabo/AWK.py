print('i Start')
print('  test.py for CircleCI')
from core.lib.emulator import *
from sys import argv
print('i from core.lib.emulator import *')
# if source != open(sys.argv[1],'r').read():
#   print(source,open(sys.argv[1],'r').read())
#   exit(1)
# if source != 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus nec odio nulla. Mauris et pharetra tortor. Aliquam maximus, mauris nec dictum convallis, enim lorem placerat quam, sit amet dapibus massa orci eget sapien. Donec vitae congue risus. Proin id fringilla lacus. Sed faucibus mi ut euismod blandit. Sed venenatis libero nec ligula ultricies finibus. Etiam turpis metus, semper in hendrerit vitae, feugiat sit amet lectus. Proin eu vehicula risus. Cras et dui vehicula, eleifend lectus sed, placerat mauris. Vestibulum felis metus, maximus vitae ornare sit amet, ultricies at nunc. Sed vestibulum sagittis vehicula. Sed sed risus tincidunt, commodo justo sed, tristique nibh. Sed maximus sem in purus gravida, ac consequat tellus posuere.':
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
