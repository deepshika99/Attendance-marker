# Attendance-marker

This code is used for maintaining attendance in a class.

Students enter their USNs in the chat in the format "1RN1NXXNNN" where X is any letter and N is any number(case insensitive). The chat history is saved as .txt file. 

From this file, the script finds the USNs and maintains only unique usns ignoring any other message.

In my Google Sheet my header row contains "USN", "Names", and dates. 

To automate the google sheet using python refer to this tutorial: https://techwithtim.net/tutorials/google-sheets-python-api-tutorial/

Limitations: I have not automated creating of date columns in header row, manually added them. 
