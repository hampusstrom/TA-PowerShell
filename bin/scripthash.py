#!/bin/python3

import sys
import csv
import hashlib

def hash(ScriptBlockText):
  try:
    hash = hashlib.sha256(ScriptBlockText.encode())
    return hash.hexdigest()
  except:
   return ''

def main():
  if len(sys.argv) < 2:
    print ("Usage: python3 scripthash.py <ScriptBlockText>")
    sys.exit(-1)

  ScriptBlockText = sys.argv[1]
  infile = sys.stdin
  outfile = sys.stdout

  r = csv.DictReader(infile)
  header = r.fieldnames
  w = csv.DictWriter(outfile, fieldnames=r.fieldnames)
  w.writeheader()

  for result in r:
   if result[ScriptBlockText] and not result['ScriptBlockHash']:
      result['ScriptBlockHash'] = hash(result[ScriptBlockText])
   w.writerow(result)
main()
