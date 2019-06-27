# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 12:31:50 2019

@author: KLAGG
"""

import numpy as np

def dates_in_myrors(
        years, months, days):
    """Formats the dates so that they have the 'yyyy-dd-mm-hhmmss' format

    :param years: the years that will formatted
    :param months: the months that will be formatted
    :param days: the days that will be formatted
    :return: conventional_dates: a 1D array of the dates in 'yyyy-dd-mm-hhmmss' format
    """
    conventional_dates = np.array([])
    for year in years:
       for month in months:
           if month == ('04' or '06' or '09' or '11'):
               for day in days[:-1]:
                   for hour in range(0, 24):
                       h = str(hour)
                       if hour < 10:
                           h = '0' + h
                       for minute in range(0, 60, 5):
                           m = str(minute)    
                           if minute < 10:
                               m = '0' + m
                           time = h + m + '00'
                           conventional_dates = np.append(conventional_dates, 
                                                          year + '-' + month + '-' + day + 
                                                          '-' + time)
                   
           if month == ('01' or '03' or '05' or '07' or '08' or '10' or '12'):
                for day in days:
                   for hour in range(0, 24):
                       h = str(hour)
                       if hour < 10:
                           h = '0' + h
                       for minute in range(0, 60, 5):
                           m = str(minute)    
                           if minute < 10:
                               m = '0' + m
                           time = h + m + '00'
                           conventional_dates = np.append(conventional_dates, 
                                                          year + '-' + month + '-' + day + 
                                                          '-' + time)
                   
           if month == ('02'):
               for day in days[:-3]:
                  for hour in range(0, 24):
                       h = str(hour)
                       if hour < 10:
                           h = '0' + h
                       for minute in range(0, 60, 5):
                           m = str(minute)    
                           if minute < 10:
                               m = '0' + m
                           time = h + m + '00'
                           conventional_dates = np.append(conventional_dates, 
                                                          year + '-' + month + '-' + day + 
                                                          '-' + time)
                   
    return conventional_dates