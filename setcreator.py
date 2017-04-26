#!/usr/bin/env python3

import json
import itemlookup
import sys
import os
from riotcall import league


def main():
    r = league.item_static()
    if r.status_code != 200:                                            # Ensure the request was successful
        sys.stderr.write("Unsuccessful API call %d\nPlease try again later" % r.status_code)
        sys.exit(1)
    else:
        allitems = r.json()                                             # take json from response

    if os.path.exists('C:\Riot Games\League of Legends\Config\Champions'):
        filefound = True
        filepath = 'C:\Riot Games\League of Legends\Config\Champions'
    else:
        filefound = False
        filepath = ''

    while not filefound:
        filepath = input('Give the path to your League of Legends Folder\n')
        filepath += '\Config\Champions'

        if not os.path.exists(filepath):
            sys.stderr.write('Invalid file location, please try again\n')
        else:
            filefound = True

    champfound = False
    filepath2=''
    while not champfound:
        champ = input('What Champion is this item set for?\nPlease Capitalize the first letter of every word\n')
        champ = champ.replace(" ", "")
        if champ == 'Wukong':
            filepath2 = filepath + '\MonkeyKing\Recommended'
        elif champ == 'Fiddlesticks':
            filepath2 = filepath + '\FiddleSticks\Recommended'
        else:
            filepath2 = filepath + "\\" + champ + '\Recommended'

        if not os.path.exists(filepath2):
            print("Error in finding champions, please try again")
        else:
            champfound = True

    validName = False
    invalidendings = ['SR', 'TT', 'DM', 'SC', 'PG']
    name = ''
    while not validName:
        name = input('What would you like to name this item set?\n')
        testName = name[-2:]
        nameisvalid = True
        for x in invalidendings:
            if x == testName:
                nameisvalid = False
                print("Invalid Name, name cannot end with SR, TT, DM, SC, or PG")
        if nameisvalid:
            validName = True

    d = {"title": name, "type": 'custom', "map": 'any', "mode": 'any', "priority": False, "sortrank": 0}

    done = False
    displaycounter = 1
    blocklist = []
    while not done:
        blockname = input('Name of item block #%d: ' % displaycounter)
        currentblock = {'type': blockname}
        itemlist = []
        itemdone = False
        while not itemdone:
            itemname = input('Item to add to this block --> ')
            itemid = itemlookup.item_name_util(itemname, allitems)
            if itemid != -1:
                thisitem = {'id': itemid}

                countdone = False
                while not countdone:
                    itemcount = input('How many would you like to add? --> ')
                    try:
                        itemcount = int(itemcount)
                        if itemcount < 1:
                            print('Error, item count must be greater than 0, try again')
                        else:
                            thisitem['count'] = itemcount
                            countdone = True

                    except (TypeError, ValueError):
                        print('Error, must input an integer, try again')

                itemlist.append(thisitem)
                itemsdone = input('Would you like to add another item to this block? (Y/n)')
                if itemsdone == 'n':
                    itemdone = True
                    currentblock['items'] = itemlist
                    displaycounter += 1
            else:
                print('Could not find item, try again')
        blocklist.append(currentblock)
        moreblock = input('Would you like to create another block? (Y/n) ')
        if moreblock == 'n':
            done = True
            d['blocks'] = blocklist

    with open(os.path.join(filepath2, name + '.json'), "w") as fout:
        fout.write(json.dumps(d, indent=4, sort_keys=True))

    print('Done!')


if __name__ == "__main__":
    main()
