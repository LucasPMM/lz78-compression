#!/usr/bin/env python3
import sys
import compression
import decompression

def output_name(input, extension):
    if len(input) == 5:
        return input[4] + extension
    return input[2].split(".")[0] + extension

if __name__ == "__main__":
    input = sys.argv

    is_compress = input[1] == "-c"
    is_decompress = input[1] == "-x"

    if is_compress:
        compression.compress(input[2], output_name(input, '.z78'))
    elif is_decompress:
        decompression.decompress(input[2], output_name(input, '.txt'))
    else:
        print('Invalid input')