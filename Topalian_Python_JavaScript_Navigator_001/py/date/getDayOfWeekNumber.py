# getDayOfWeekNumber.py

import datetime as dt

def getDayOfWeekNumber():
    now = dt.datetime.now()

    # sunday returns as 6
    dayOfWeekNumber = now.weekday()

    # adjust so that sunday returns as 0
    dayOfWeekNumber = (dayOfWeekNumber + 1) % 7

    # adjust so that sunday returns as 1
    dayOfWeekNumberAdjusted = dayOfWeekNumber + 1

    return dayOfWeekNumberAdjusted

# print(getDayOfWeekNumber())
# input('')

#--------------------#
# If today is Wednesday, it returns:
# 4
#--------------------#

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
# getDayOfWeekNumber.py
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian

#********************#

