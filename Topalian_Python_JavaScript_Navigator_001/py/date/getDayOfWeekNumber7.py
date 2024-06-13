# getDayOfWeekNumber7.py

import datetime as dt

def getDayOfWeekNumber7():
    now = dt.datetime.now()

    # monday is 0, sunday is 6
    dayOfWeekNumber = now.weekday()

    # adjust so that monday is 1, sunday is 7
    dayOfWeekNumberAdjusted = dayOfWeekNumber + 1

    return dayOfWeekNumberAdjusted

# print(getDayOfWeekNumber7())
# input('')

#--------------------#
# If today is Wednesday, it returns:
# 3
#--------------------#

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
# getDayOfWeekNumber7.py
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian

#********************#

