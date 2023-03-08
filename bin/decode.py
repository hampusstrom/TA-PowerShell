#!/bin/python3

import sys
import csv
from base64 import b64decode,b64encode

def decode(encodedCommand):
  try:
    return (b64decode(encodedCommand).decode('UTF-16LE'))
  except:
   return ''

def main():
  if len(sys.argv) < 2:
    print ("Usage: python3 decode.py <encodedCommand>")
    sys.exit(-1)

  encodedCommand = sys.argv[1]
  infile = sys.stdin
  outfile = sys.stdout

  r = csv.DictReader(infile)
  header = r.fieldnames
  w = csv.DictWriter(outfile, fieldnames=r.fieldnames)
  w.writeheader()

  for result in r:
   if result[encodedCommand] and not result['decodedCommand']:
      result['decodedCommand'] = decode(result[encodedCommand])
   w.writerow(result)
main()
