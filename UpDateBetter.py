# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 09:22:22 2023

@author: julia.m.waldsmith
"""

# Python 3 (may need to switch to 2 to be PydroGIS compatible) 

# Different approach using a replacement method
# https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file
# https://www.geeksforgeeks.org/get-yesterdays-date-using-python/
# Modified with chatgpt https://chat.openai.com/c/8b176052-f39d-4e33-944f-28fc3cde8fde

# import modules
import re
from datetime import date
from datetime import timedelta

def replace_dates(text):
    today_date = date.today()
    #yesterday_date = date.today() - timedelta(days=1)
    # Define date patterns
    date_patterns = [r'\d{1,2}/\d{1,2}/\d{4}', r'\d{4}-\d{2}-\d{2}'] 
    # Iterate through date patterns and replace them with today's date
    for pattern in date_patterns:
        text = re.sub(pattern, today_date.strftime("%Y-%m-%d"), text)
        #text = re.sub(pattern, yesterday_date.strftime("%Y-%m-%d"), text)
    return text

# open file to read, replace with new date

file_path = 'pydro_resid.bat'

with open(file_path,'r') as file:
    batch_content = file.read()
   
# Replace dates with today's date  
modified_content = replace_dates(batch_content)

# Write the modified content back to the batch file  
with open(file_path,'w') as file:
    file.write(modified_content)

print("Dates updated!")

