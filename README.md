# Attendance-marker

This code is used for maintaining attendance in a class.

Students enter their USNs in the chat in the format "1RN1NXXNNN" where X is any letter and N is any number(case insensitive). The chat history is saved as .txt file. 

From this file, the script finds the USNs and maintains only unique usns ignoring any other message.

In my Google Sheet my header row contains "USN", "Names", and dates. Example excel sheet given.

To automate the google sheet using python refer to this tutorial: https://techwithtim.net/tutorials/google-sheets-python-api-tutorial/


Edit: 
1. Update 10/09/2020 Fixed "Limitations: I have not automated creating of date columns in header row, manually added them." 
Dates get automatically added and added a new feature of creating a list of absentees in worksheet2 in the workbook. Trying to clean up the code even further.


