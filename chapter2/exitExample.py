# import sys
from sys import exit

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        # sys.exit()
        exit()
    print('You typed ' + response + '.')
