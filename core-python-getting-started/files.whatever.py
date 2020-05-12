#!/usr/bin/env python3

import sys

try:
    if len(sys.argv) != 2:
        raise ValueError('Need to supply a file name.')

    fn = sys.argv[1]
    print(f"Reading from `{fn}`...")

    f = open(fn, 'rt', encoding='utf-8')
    
    for line in f:
        print(line)
except Exception as err:
    print(err)
finally:
    f.close()