import mintapi
import pandas as pd
import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials
import keyring


mint = mintapi.Mint(
    keyring.get_password("Mint", "username"),
    keyring.get_password("Mint",keyring.get_password("Mint", "username")),
 
    # Optional parameters
    mfa_method='email',  # Can be 'sms' (default), 'email', or 'soft-token'.
                       # if mintapi detects an MFA request, it will trigger the requested method
                       # and prompt on the command line.
    headless=False,  # Whether the chromedriver should work without opening a
                     # visible window (useful for server-side deployments)
    mfa_input_callback=None,  # A callback accepting a single argument (the prompt)
                              # which returns the user-inputted 2FA code. By default
                              # the default Python `input` function is used.
    session_path=None, # Directory that the Chrome persistent session will be written/read from.
                       # To avoid the 2FA code being asked for multiple times, you can either set
                       # this parameter or log in by hand in Chrome under the same user this runs
                       # as.
    imap_account=None, # account name used to log in to your IMAP server
    imap_password=None, # account password used to log in to your IMAP server
    imap_server=None,  # IMAP server host name
    imap_folder='INBOX',  # IMAP folder that receives MFA email
    wait_for_sync=False,  # do not wait for accounts to sync
    wait_for_sync_timeout=300,  # number of seconds to wait for sync
)

transactions = mint.get_transactions()
transactions = transactions.drop(["labels", 'notes', 'original_description'], axis=1)
transactions.loc[(transactions.transaction_type == 'debit'), 'transaction_type'] = 'Expense'
transactions.loc[(transactions.transaction_type == 'credit'), 'transaction_type'] = 'Income'
transactions = transactions[transactions.category != 'credit card payment']

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('mintCredentials.json', scope)
client = gspread.authorize(creds)
# Send the data to google sheets
spreadsheet_key = keyring.get_password("Mint", "google_sheets_key")
d2g.upload(transactions,spreadsheet_key,"RAW_DATA",credentials=creds,row_names=True)
