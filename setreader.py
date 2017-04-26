#!/usr/bin/env python3

import json
import itemlookup
import sys
import os


# ItemConverter: opens given file and prints information in human readable way
# Args: s - path to file
def itemconverter(s):
    with open(s) as json_data:
        data = json.load(json_data)
        print(data['champion'] + ': ' + data['title'] + '\n')       # Print header
        for r in data['blocks']:                                       # todo: Fix to flow in any length array
            print(r['type'])
            s = r['items']
            for w in s:
                s = itemlookup.lookuputil(w['id'])                  # Pass ID to RESTful call function
                if s:
                    print('\t', end="")
                    print(s)
            print('\n')


def itemconverterfile(s, f):
    with open(s) as json_data:
        file = open(f, "w");
        data = json.load(json_data)
        file.write(data['champion'] + ': ' + data['title'] + '\n')
        for x in range(0, 4):
            r = data['blocks'][x]
            file.write(r['type'])
            s = r['items']
            for w in s:
                s = itemlookup.lookuputil(w['id'])
                if s:
                    file.write('\t', end="")
                    file.write(s)
            file.write('\n')
    file.close()


# Main method of the program, only argument to pass in is path to the item set to read
# passes to itemconverter() if correct
def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        usage()
    elif not os.path.isfile(sys.argv[1]):
        sys.stderr.write("File does not exist\n")
        usage()
    elif len(sys.argv) == 2:
        itemconverter(sys.argv[1])


def usage():
    sys.stderr.write("Usage: setreader [file name] \n")


if __name__ == "__main__":
    main()
