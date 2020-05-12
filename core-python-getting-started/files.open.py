#!/usr/bin/env python3

import sys

try:
    print(f"Default File Encoding: {sys.getdefaultencoding()}")
    f = open('things.txt', mode='wt')
    f.write("Testing file write!\n")
except Exception as e:
    pass
finally:
    f.close()