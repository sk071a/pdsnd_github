# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 15:13:26 2020

@author: sk071a
"""
# Analyze Bikeshare Data to provide Key Analysis
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': '/Users/sk071a/Documents/UDACITY/Programming for Data Science/bikeshare-2/chicago.csv',
              'new york city': '/Users/sk071a/Documents/UDACITY/Programming for Data Science/bikeshare-2/new_york_city.csv',
              'washington': '/Users/sk071a/Documents/UDACITY/Programming for Data Science/bikeshare-2/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = ''
    while city not in ['chicago','new york city','washington']:
        print('Which city we want to analyze? (Type :"Chicago" or "New York City" or "Washington")')
        city = input().lower()

    month = ''
    while month not in ['all','january','february','march','april','may','june']:
        print('Which month we want to analyze? (Type : "All" to analyze all months or individual month by "January" or "February" or "March" or "April" or "May" or "June")')
        month = input().lower()

    day = ''
    while day not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        print('Which day of the week we want to analyze? (Type : "All" to analyze all  days or day by "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday" or "Saturday" or "Sunday")')
        day = input().lower()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    most_common_month = df['month'].mode()[0]
    if most_common_month ==1:
        print('Most Common Month to travel is January.')
    if most_common_month ==2:
        print('Most Common Month to travel is Febuary.')
    if most_common_month ==3:
        print('Most Common Month to travel is March.')
    if most_common_month ==4:
        print('Most Common Month to travel is April.')
    if most_common_month ==5:
        print('Most Common Month to travel is May.')
    if most_common_month ==6:
        print('Most Common Month to travel is June.')


    # display the most common day of week

    print('Most Commom Day of Week to travel is',df['day_of_week'].mode()[0])

    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    if common_hour >12:
        new_hour = common_hour - 12
        print('Most Common Hour to travel is',new_hour,'PM.')
    if common_hour <12:
        print('Most Common Hour to travel is',common_hour,'AM.')
    if common_hour ==12:
        print('Most Common Hour to travel is',common_hour,'PM.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    print('Most Commomly used of Start Station is',df['Start Station'].mode()[0],'.')

    # display most commonly used end station

    print('Most Commomly used of End Station is',df['End Station'].mode()[0],'.')

    # display most frequent combination of start station and end station trip

    df['Start_End'] = 'Start Station is "' + df['Start Station'] + '" and the End Station is "' + df['End Station'] +'"'
    print('Most Commomly used',df['Start_End'].mode()[0],'.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = np.sum(df['Trip Duration'])
    T_hours = total_duration // 60
    T_mins = total_duration % 60
    print('Total Travel Time is', total_duration,'mintues or',T_hours,'hours and',T_mins,'minutes.')

    # display mean travel time

    Average_duration = round(np.mean(df['Trip Duration']),2)
    A_hours = Average_duration // 60
    A_mins = Average_duration % 60
    print('Average Travel Time is', Average_duration,'mintues or',A_hours,'hours and',A_mins,'minutes.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of User Type:')
    print(df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df.columns:
        print('Counts of Gender:')
        print(df['Gender'].value_counts())
    else:
        print('NO GENDER INFO IS AVAILABLE')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('The earliest birth year is', int(np.min(df['Birth Year'])))
        print('The most recent birth year is', int(np.max(df['Birth Year'])))
        print('The most common birth year is', int(df['Birth Year'].mode()[0]))
    else:
        print('NO Birth Year INFO IS AVAILABLE')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_date(df):
    """Display 5 rows at a time."""

    print('Here is the first 5 rows of the raw data')
    df['row']=np.arange(len(df))
    i=0
    j=5
    while True:
        df1=df[(df.row >=i) & (df.row <j)]
        print(df1.iloc[:, 0:-1])
        more = input('\nWould you like to see the next 5 rows? Enter yes or no.\n')
        if more.lower() != 'yes' and more.lower() != 'y':
            break
        else:
            i+=5
            j+=5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_date(df)



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes' and restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
