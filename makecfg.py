#!/bin/python3

import json
import sys

def main():
    if len(sys.argv) != 3:
        print("Invalid data, please try again")
        return
    data = {
            "url": sys.argv[1],
            "name": sys.argv[2]
            }

    with open("config.json", "w") as cfg_file:
        json.dump(data, cfg_file)
    print("Done!")

main()
