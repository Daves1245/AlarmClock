#!/bin/python3

"""
file: alarm.py
Grab my work schedule using Google Sheets API, and parse
it for shifts where I work. Then set an appropriate wakeup
time on my raspberry pi while I work out getting a 'real'
alarm clock.
"""

# TODO grab info (url, name) from config.json instead of url.txt

import pandas as pd
import gspread
import numpy as np
import gsheets
from oauth2client.service_account import ServiceAccountCredentials

# When alarm gets set off
def callback():
    # TODO
    return

def get_url(filename):
    ret = None
    with open(filename, "r") as f:
        ret = f.read()
    return ret

def get_shift_starts(worksheet, name):
    shifts = None
    ret = []
    for index, row in worksheet.iterrows():
        """if index == 0:
            dates = row.array
        if index == 1:
            shifts = row
        if row[row == "David"].size > 0 and row[row == "David"].index[0] != -1:
            print(row[row == "David"].index[0])
            """
        for entry in row.array:
            if entry == name:
                ret.append(row[1])
    return ret

scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('alarm_clock_creds.json', scope)
gc = gspread.authorize(credentials)

URL = get_url('url.txt')
gsheet = gc.open_by_url(URL)

spreadsheets = [spreadsheet.get_all_values() for spreadsheet in gsheet.worksheets()]
headers = [data.pop(0) for data in spreadsheets]
data = [pd.DataFrame(spreadsheets[i], columns = headers[i]) for i in
        range(0, len(spreadsheets))]

schedule_sheet = data[0]

times = get_shift_starts(schedule_sheet, "David")
print(times)
