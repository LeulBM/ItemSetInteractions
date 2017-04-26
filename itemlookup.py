#!/usr/bin/env python3

import sys
import json
from riotcall import league
from pprint import pprint

def usage():
    sys.stderr.write("Usage: itemlookup [id number] \n")


def lookup(id):
    r = league.item_static(id)
    datadict = json.loads(r.text)
    if r.status_code == 200:
        print(datadict['name'])
    else:
        sys.stderr.write("Non-successful Request %d\n" % r.status_code)


def lookuputil(id):
    r = league.item_static(id)
    datadict = json.loads(r.text)
    if r.status_code == 200:
        return datadict['name']


# Item by name - Calls the static item data, and searches all entries for a name
# matching the entered value. If it is found, the corresponding id is returned
# otherwise the value -1 is returned to represent a failed response
# Args: iname - name of item
def item_by_name(iname):
    r = league.item_static()
    if r.status_code != 200:                                            # Ensure the request was successful
        sys.stderr.write("Unsuccessful API call %d\n" % r.status_code)
    else:
        allitems = r.json()                                             # take json from response
        for x, y in allitems['data'].items():
            if 'name' in y:                                             # check if the current dict has a name key
                currval = y['name']                                     # compare values
                if plaintext_string(currval) == plaintext_string(iname):
                    return x
    return -1


# Item by name - Utility version of item_by_name, extracts API call to save time
# Args: iname - name of item
#       source - json output from response
def item_name_util(iname, source):
    for x, y in source['data'].items():
        if 'name' in y:                                              # check if the current dict has a name key
            currval = y['name']                                      # compare values
            if plaintext_string(currval) == plaintext_string(iname):
                return x
    return -1


# Plaintext String - converts given string to all uppercase and removes spaces to allow for
# wider breath of acceptable options for user input
# Args: comples- unsimplified string
def plaintext_string(complex):
    fixing = complex
    fixing = fixing.replace(" ", "")
    fixing = fixing.upper()
    return fixing


def main():
    if len(sys.argv) != 2:
        usage()

    elif not sys.argv[1].isdigit():
        usage()

    else:
        lookup(int(sys.argv[1]))


if __name__ == "__main__":
    main()
