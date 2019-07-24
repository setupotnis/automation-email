import gspread
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials
import requests
from bs4 import BeautifulSoup
import smtplib


scope = ["https://spreadsheets.google.com/feeds",
"https://www.googleapis.com/auth/spreadsheets",
"https://www.googleapis.com/auth/drive.file",
"https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet= client.open("makeup-company-list").sheet1

data = sheet.get_all_records()

emails = sheet.col_values(9)

def send_email():
    #for email in emails:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('tejocosmetics@gmail.com', 'google_pass')

        subject = 'Subject: Valuable Busines Opportunity'
        body = 'template'

        msg = 'Subject: {0} \n\n {1}'.format(subject, body)

        server.sendmail(
            'tejocosmetics@gmail.com',
            'setupotnis@gmail.com',
            msg
        )

        print('EMAIL HAS BEEN SENT')
        server.quit()

send_email()

#print(type(column))
#pprint(len(column))