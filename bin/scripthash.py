#!/bin/python3

import sys
import csv
import hashlib

def hash(ScriptBlockText):
    if isinstance(ScriptBlockText, str):
        try:
            ScriptBlockText = ScriptBlockText.encode("utf-16-le")
        except:
            try: 
                ScriptBlockText = ScriptBlockText.encode("utf8")
            except:
                raise Exception("Unable to encode unicode object.")
        
    try:
        hash = hashlib.sha256(ScriptBlockText)
        return hash.hexdigest()
    except Exception as e:
        print(e)
        return ''

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripthash.py <ScriptBlockText>")
        sys.exit(-1)

    ScriptBlockText = sys.argv[1]
    infile = sys.stdin
    outfile = sys.stdout

    rows = csv.DictReader(x.replace('\0','') for x in infile)
    headers = rows.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=headers)
    writer.writeheader()

    for row in rows:
        if row[ScriptBlockText] and not row['ScriptBlockHash']:
            row['ScriptBlockHash'] = hash(row[ScriptBlockText])
        writer.writerow(row)
main()
