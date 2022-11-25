#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import packages 
import time
from datetime import datetime
import pandas as pd
import numpy as np

print('-'*40)
print('Hello! Lets explore the chicago.csv dataset!')
print('-'*40)

# Read "chicago.csv" file
df_1 = pd.read_csv('chicago.csv')

# Check the shape of the file
print('Number of rows and columns in the dataset:\n', df_1.shape)

# See general info about the dataset
print('The types of values in each column in the dataset:\n')
df_1.info()

# Check the missing values
print('Any missing values?\n', df_1.isnull().sum())

# See the 5 first rows
print('The 5 first rows in the dataset:\n', df_1.head())

# Calculate descriptive statistics for the data
print('Descriptive statistics:\n', df_1.describe())

print('-'*40)
print('Hello! Lets explore the new_york_city.csv dataset!')
print('-'*40)

# Read "new_york_city.csv" file
df_2 = pd.read_csv('new_york_city.csv')

# Check the shape of the file
print('Number of rows and columns in the dataset:\n', df_2.shape)

# See general info about the dataset
print('The types of values in each column in the dataset:')
df_2.info()

# Check the missing values
print('Any missing values?\n', df_2.isnull().sum())

# See the 5 first rows
print('The 5 first rows in the dataset:\n', df_2.head())

# Calculate descriptive statistics for the data
print('Descriptive statistics:\n', df_2.describe())

print('-'*40)
print('Hello! Lets explore the washington.csv dataset!')
print('-'*40)
# Read "washington.csv" file
df_3 = pd.read_csv('washington.csv')

# Check the shape of the file
print('Number of rows and columns in the dataset:\n', df_3.shape)

# See general info about the dataset
print('The types of values in each column in the dataset:')
df_3.info()

# Check the missing values
print('Any missing values?\n', df_3.isnull().sum())

# See the 5 first rows
print('The 5 first rows in the dataset:\n', df_3.head())

# Calculate descriptive statistics for the data
print('Descriptive statistics:\n', df_3.describe())

# Gender and Birth Year columns are missing in the washington.csv dataset
# Type of the Birth Year variable is float, should be integer 
# Outliers identified in the Birth Year variable 
# These points should be taken into account during further analysis

# There are missing values in all three datasets. Drop out all observations with missing values
df_1 = df_1.dropna(axis = 0)
df_2 = df_2.dropna(axis = 0)
df_3 = df_3.dropna(axis = 0)

# Double check for the missing values
print('Double check wether any missing values in chicago.csv?\n', df_1.isnull().sum())
print('Double check wether any missing values in ew_york_city.csv\n', df_2.isnull().sum())
print('Double check wether any missing values in washington.csv\n', df_3.isnull().sum())

# Saving the dataframe
df_1.to_csv('chicago1.csv')
df_2.to_csv('new_york_city1.csv')
df_3.to_csv('washington1.csv')

print('-'*40)
# Create some lists and dictionary to load the dataset 
CITY_DATA = {'chicago': 'chicago1.csv',
              'new york': 'new_york_city1.csv',
              'washington': 'washington1.csv'}
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june','all']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    
    # get user input for city (chicago, new york city, washington)
    while True:
        city = input('Would you like to see data for Chicago, New York, or Washington?\n').lower()
        if city in CITY_DATA.keys():
            break
        else:
            print('Invalid Input!! Please input the correct namme. It can be either Chicago, New York, or Washington')
   
    # get user input for month (all, january, february, ... , june)
    months = MONTHS
    while True:
        month = input('Please, select the month (January, February, March, April, May, June) to filter the data or fill in (all) for not filtering\n').lower()
        if month in months:
            break
        else:
            print('Invalid Input!! Please input the correct namme')
    
    # get user input for day of week (all, monday, tuesday, ... sunday) 
    days = DAYS
    while True:
        day = input('Please, select the day of week(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) to filter or fill in (all) for not filtering:\n').lower()
        if day in days:
            break
        else:
            print('Invalid Input!! Please input the correct namme')

    
    return city, month, day


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
    
    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month from Start Time to create new column
    df['month'] = df['Start Time'].dt.month_name()
    
    # Extract day of week from Start Time to create new column
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month
    if month != 'all':
        df = df[df['month'].str.startswith(month.title())]

    # Filter by day of week
    if day != 'all':
        df = df[df['day_of_week'].str.startswith(day.title())]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most popular month
    df['month'] = df['Start Time'].dt.month_name()
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # display the most popular day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day:', popular_day)

    # display the most popular start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station) 

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    start_end_combination = df.groupby(['Start Station','End Station'])
    popular_trip = start_end_combination.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', popular_trip)
        
    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = round(df['Trip Duration'].sum()/3600,2)
    print('Total travel time:', total_travel_time,' hours')
    
    # display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean()/60,2)
    print('Mean travel time:', mean_travel_time, ' minutes')
    
    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Users types in the dataset:\n', user_types)
    
    # Display counts of gender 
    # Columns Gender and Birth Year do not appear in washington.csv dataset. We need to apply filter
    if city != 'washington':
        print('Counts of Gender:\n', df['Gender'].value_counts())
         
    # Display earliest, most recent, and most common year of birth
        # change the type of the Birth Year variable
        df['Birth Year'] = df['Birth Year'].astype(int)
        
        print('Earliest Year of Birth:', df['Birth Year'].min())
        print('Most Recent Year of Birth:', df['Birth Year'].max())
        print('Most Common Year of Birth:', df['Birth Year'].mode()[0]) 
        
    # Display oldest, youngest, most common, and average age
        currentYear = datetime.now().year
        age = round(currentYear - df['Birth Year'],0)
        
        print('Oldest Age:', age.max())
        if age.max() > 110:
            print ('The maximum value of age is {}. It seems to be an outlier!!'.format(age.max()))
        print('Youngest Age:', age.min())
        if age.min() < 3:
            print ('The minimum value of age is {}. It seems to be an outlier!!'.format(age.min()))
        print('Most Common Age:', age.mode()[0])
        print('Average Age:', round(age.mean(),1))
        
    if city == 'washington':
        print('No filter with Gender is allowed in Washington city!')
        print('No filter with Birth Year is allowed in Washington city!')

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)

# Create a function which shows 5 rows from the data repeatedly
def show_5_rows(df):
    show_data = input('Would you like to see 5 rows of data? Please enter yes or no?').lower()
    start_loc = 0
    while show_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5,:])
        start_loc += 5
        show_data = input('Would you like to see 5 rows of data? Please enter yes or no?').lower()
        
    return df

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_5_rows(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

