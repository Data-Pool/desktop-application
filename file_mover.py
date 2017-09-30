from sys import argv, exit
from os import path, listdir, rename
from time import sleep

if len(argv) < 3:
    print('Two directories need to be inputed')
    exit()

if not path.isdir(argv[1]) or not path.isdir(argv[2]):
    print('Not a directory')

while 1:
    files = listdir(argv[1])
    for f in files:
        fn, fext = path.splitext(f)
        if fext == '.dpl':
            rename(path.join(argv[1], f), path.join(argv[2], f))
    sleep(1)
