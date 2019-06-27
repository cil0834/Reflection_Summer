# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 12:31:50 2019

@author: KLAGG
"""

import numpy as np

def dates_in_myrors(
        years, months, step=5):
    """Formats the dates so that they have the 'yyyy-dd-mm-hhmmss' format
    
    :param years: the years that will formatted
    :param months: the months that will be formatted
    :param step: the interval in minutes that a new time is generated
    :return: conventional_dates: a 1D array of the dates in 'yyyy-dd-mm-hhmmss' format
    """
    # Create the numpy array that will hold the dates in yyyy-dd-mm-hhmmss format
    conventional_dates = np.array([])
    
    for year in years:
       for month in months:
           # If there are only 30 days in the month
           if month == ('04' or '06' or '09' or '11'):
               for day in range(1, 31):
                   day = str(day)
                   for hour in range(0, 24):
                       h = str(hour)
                       if hour < 10:
                           h = '0' + h
                       # Step size is 5 because we only want every 5 minutes
                       for minute in range(0, 60, step):
                           m = str(minute)    
                           if minute < 10:
                               m = '0' + m
                           time = h + m + '00'
                           conventional_dates = np.append(conventional_dates, 
                                                          year + '-' + month + '-' + day + 
                                                          '-' + time)
           # If there are 31 days in the month
           if month == ('01' or '03' or '05' or '07' or '08' or '10' or '12'):
                for day in range(1, 32):
                   day = str(day)
                   for hour in range(0, 24):
                       h = str(hour)
                       if hour < 10:
                           h = '0' + h
                       for minute in range(0, 60, step):
                           m = str(minute)    
                           if minute < 10:
                               m = '0' + m
                           time = h + m + '00'
                           conventional_dates = np.append(conventional_dates, 
                                                          year + '-' + month + '-' + day + 
                                                          '-' + time)
           # If not a leap year
           if month == ('02') and (int(year) % 4 != 0):
               for day in range(1, 29):
                  day = str(day)
                  for hour in range(0, 24):
                       h = str(hour)
                       if hour < 10:
                           h = '0' + h
                       for minute in range(0, 60, step):
                           m = str(minute)    
                           if minute < 10:
                               m = '0' + m
                           time = h + m + '00'
                           conventional_dates = np.append(conventional_dates, 
                                                          year + '-' + month + '-' + day + 
                                                          '-' + time)
           # If leap year
           if month == ('02') and (int(year) % 4 == 0):
               for day in range(1, 30):
                  day = str(day)
                  for hour in range(0, 24):
                       h = str(hour)
                       if hour < 10:
                           h = '0' + h
                       for minute in range(0, 60, step):
                           m = str(minute)    
                           if minute < 10:
                               m = '0' + m
                           time = h + m + '00'
                           conventional_dates = np.append(conventional_dates, 
                                                          year + '-' + month + '-' + day + 
                                                          '-' + time)
                   
    return conventional_dates


