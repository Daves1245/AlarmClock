#!/bin/python3

from parse import *
import gspread
import pandas
from oauth2client.service_account import ServiceAccountCredentials
from optparse import OptionParser

url_path = 'url.txt'
credentials_path = 'creds.json'
verbose = False

scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path)

# Grab the url in url.txt
def get_url():
    ret = None
    with open(url_path, 'r') as file:
        ret = file.read()
    return ret

# The main alarm clock function 
# TODO use cron jobs or make python daemon?
def clock():
    return

def prepare_times(times):
    for t in times:
        """
        if t <= '6:30AM':
            do NOT wake me up earlier than 5:30
        else:
            times[t] -= time_shift (1hr?)
        """

def main():
    argparser = OptionParser()
    argparser.add_option("-u", "--url", dest = "url",
            help = "Pass URL as an argument")
    argparser.add_option("-v", "--verbose", dest = "verbose",
            default = False, help = "Turn on verbose mode")
    (options, args) = argparser.parse_args()
    client = gspread.authorize(creds)
    url = get_url()
    if url == None: # if url:
        print("Please write a valid url into url.txt")
        return
    sheet = client.open_by_url(url)
    schedule = sheet.get_worksheet(0)
    times = parse(schedule, "David")
    wakeup_times = prepare_times(times)
    print(times)

main()
