#!/bin/python3

import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np

scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('alarm_clock_creds.json', scope)
gc = gspread.authorize(credentials)

URL = get_url('url.txt')
gsheet = gc.open_by_url('')

spreadsheets = [spreadsheet.get_all_values() for spreadsheet in gsheet.worksheets()]
headers = [data.pop(0) for data in spreadsheets]
data = [pd.DataFrame(spreadsheets[i], columns = headers[i]) for i in
        range(0, len(spreadsheets))]

schedule_sheet = data[0]

# dates = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
# dates = None

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

times = get_shift_starts(schedule_sheet, "David")
print(times)
