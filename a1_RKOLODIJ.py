#!/usr/bin/env python3
''' template for ops435 assignment 1 script
    put your script level docstring here...
    you can have more than one line of docstring.
    Please personlize the following author declaration:
-----------------------------------------------------------------------
OPS435 Assignment 1 - Winter 2021
Program: a1_RKOLODIJ.py (replace [Seneca_name] with your Seneca User name)
Author: Rostyslav Kolodij
The python code in this file (a1_[Seneca_name].py) is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
import os
import sys

def leap_year(obj):
    if (( obj%400 == 0) or (( obj%4 == 0 ) and ( obj%100 != 0))):
        return True
    else:
        return False

def sanitize(obj1,obj2):
    if (obj1 == ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        return(obj1)
    else: 
        numeric_filter = filter(str.isdigit, obj1)
        obj2 = "".join(numeric_filter)
        return(obj2) 
    
def size_check(obj,intobj):
    if len(obj) ==  intobj:
        return True
    else:
        return False

def range_check(obj1, obj2):
    if int(obj1) in range(obj2[0], obj2[1]):
        status = True
    else:
        status = False   
    return status
    
def usage():    
    
    return('Usage: a1_RKOLODIJ.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD')

if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   print('Sanitized user data:', dob)
   # setp 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong data entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: Wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   print("Your date of birth is:", new_dob)  
