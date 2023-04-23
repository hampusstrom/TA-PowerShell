#!/bin/python3

import sys
import csv
from base64 import b64decode

# Pythons b64 library expects a b64 string made up of multiples of four
# The base64 spec says that any b64 string not consisting of multiples of four should be padded with '='
# at the end of the string until this statement is true.


def get_padded_b64(encodedCommand):
    return (encodedCommand + '=' * ((4 - len(encodedCommand) % 4) % 4))


def decode_b64_bytes(encodedCommand):
    try:
        utf_encoded_string = encodedCommand.decode("utf-16-le")
        return utf_encoded_string
    except Exception as e:
        try:
            utf_encoded_string = encodedCommand.decode("utf8")
            return utf_encoded_string
        except Exception as er:
            print(er)
            return '-'


def decode(encodedCommand):
    # Avoids padding errors
    encodedCommand = get_padded_b64(encodedCommand)
    try:
        decodedBytes = b64decode(encodedCommand)
    except Exception as e:
        return '-'

    # We convert to utf8 as powershell's default UTF16-LE contains null bytes.
    # The csv module in python 3.7 that Splunk uses, doesn't like them.
    return decode_b64_bytes(decodedBytes)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 decode.py <EncodedCommand Field Name>")
        sys.exit(-1)

    encodedCommand = sys.argv[1]
    infile = sys.stdin
    outfile = sys.stdout

    rows = csv.DictReader(infile)
    headers = rows.fieldnames
    w = csv.DictWriter(outfile, fieldnames=headers)
    w.writeheader()

    for row in rows:
        if row[encodedCommand] and not row['decodedCommand']:
            row['decodedCommand'] = decode(row[encodedCommand])
        w.writerow(row)


main()
