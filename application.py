import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date, datetime, timedelta

### getting the sheet
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("your google sheets name").sheet1

##getting chat txt file
chatFile = open(r"location of your .txt file")
chatContent = chatFile.read()

###today's and yesterday's date
today = datetime.today().strftime('%d-%m-%Y')
yesterday = datetime.strftime(datetime.now() - timedelta(1), '%d-%m-%Y')

###regex pattern and find the usns
usn = re.compile(r'(1(8|7|6|5)[a-zA-Z]{2}\d\d\d)')
mo = usn.findall(chatContent)

#####get usns as unique list
usns = []
for number in mo:
    usns.append(number[0])
usns = [x.lower() for x in usns] #USNs to lower case
check = set(usns)
usns = (list(check))

####get all details of file as list of dicts
records = sheet.get_all_records(empty2zero=True)
for dicts in records:
    dicts[today] = int(dicts[today]) #make all as ints
    dicts['USN'] = dicts['USN'].lower() #make usns to lower case

### updating USN in the records
for dicts in records:
    usn1 = dicts['USN']
    for uni in usns:
        if uni == usn1[3:]:
            dicts[today] = dicts[yesterday]+1
            break
        dicts[today] = dicts[yesterday]

cell = sheet.find(today) #find cell with today's date so column can be updated
marking = [] #list of attendance for today eg - [1,1,0,1...]
for dicts in records:
    marking.append(dicts[today])

### update the attendance in google sheet
for i in range(2, len(records)+1):
    sheet.update_cell(i, cell.col, marking[i-2])
