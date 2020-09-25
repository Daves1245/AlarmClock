"""
parse.py: Given a sheets and name,
parse the worksheet for the name
and return a dictionary of date->time.

This file should be editted if you want
to use this yourself - my work schedule
is laid out very specifically.
"""

import re

# TODO make this quota friendly
def parse(worksheet, name):
    ret = {}
    for c in range(5, 11):
        for r in range(4, 16):
            cell = worksheet.cell(row = r, col = c).value
            if cell == name:
                ret[worksheet.cell(row = 2, col = c).value] = worksheet.cell(row = r, col = 2).value
            if name in cell and "start" in cell:
                tmp = re.search("[0-9]+(:[0-9]+)?(\s)?(AM|PM|am|pm)?", line)
                if not tmp:
                    # TODO better error state
                    print("UNKNOWN START TIME!")
                    continue
                ret[worksheet.cell(row = 2, col = c).value] = tmp.group()
    return ret
