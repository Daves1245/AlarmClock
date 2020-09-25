#!/bin/python3

import gspread
import pandas
from oauth2client.service_account import ServiceAccountCredentials

url_path = 'url.txt'
credentials_path = 'alarm_clock_creds.json'
cache_path = 'cache.json'

scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path)

# Grab the url in url.txt
def get_url():
    ret = None
    with open(url_path, 'r') as file:
        ret = file.read()
    return ret

# Parse the worksheet and return the shift start times
# TODO move to separate file
# TODO make this quota friendly
import re
def parse(worksheet, name):
    client = gspread.authorize(creds)
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

def main():
    client = gspread.authorize(creds)
    url = get_url()
    if url == None: # if url:
        print("Please write a valid url into url.txt")
        return
    sheet = client.open_by_url(url)
    schedule = sheet.get_worksheet(0)
    times = parse(schedule, "David")
    print(times)

main()
