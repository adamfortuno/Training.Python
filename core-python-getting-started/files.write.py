#!/usr/bin/env python3

import sys

enc = 'utf-8'
filename = 'sandbox.txt'

#####################################################################
# Writes
#####################################################################

## Write some stuff
writeTo_handle = open(filename, mode='wt', encoding=enc)
charsWritten = writeTo_handle.write('This is a line of output.\n')

stuff = ['i love my moolities\n',
    'i love my bean bean too\n',
    'i have a great family\n',
    'and, i have pretty good friends\n',
]
writeTo_handle.writelines(stuff)

writeTo_handle.close()

#####################################################################
# Reads
#####################################################################

## Reading from the file
readFrom_handle = open(filename, 'rt', encoding=enc)
print(f'Ex 1: {readFrom_handle.read(charsWritten)}')

## Adding a carriage return to the line on read
readFrom_handle.seek(0)
print(f'Ex 2: {readFrom_handle.readline()}')

## Import all lines into a list
readFrom_handle.seek(0)
lines = readFrom_handle.readlines()
print(f"Ex 3: {lines}")

readFrom_handle.close()