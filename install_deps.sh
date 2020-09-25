#!/bin/bash

echo "Installing python dependencies..."
sudo -H pip3 install gspread pandas oauth2client google-api-python-client sense_hat
sudo -H pip3 install --upgrade google-api-python-client oauth2client
