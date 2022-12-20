# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# imports entire gspread lib
import gspread 
# imports creditals class from google auth
from google.oauth2.service_account import Credentials
# all constant variable in caps
# the scope lists the apis that the program should access in order for the program to run
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# below is essentially accessing the sheet
CREDS = Credentials.from_service_account_file('creds.json')   
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# access sales tab in worksheet 
sales = SHEET.worksheet('sales')

# key take away from above is that you need these settings to access our spreadsheet data 
# pull values from sales tab
data = sales.get_all_values()

print(data)