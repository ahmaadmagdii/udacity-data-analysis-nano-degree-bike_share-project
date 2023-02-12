import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        print('please choose your city:')
        print('\n 1. chicago 2. new york city 3. washington')
        city = input().lower()

        if city not in CITY_DATA.keys():
            print('sorry, i didnt understand that, please try again')
    

    # get user input for month (all, january, february, ... , june)
    months_ = {'january':1 , 'february':2 , 'march':3 , 'april':4 , 'may':5 , 'june':6 , 'all':7}
    month = ''
    while month not in months_.keys():
        print('please enter the month')
        month = input().lower()

        if month not in months_.keys():
            print('sorry, i didnt understand that, please try again')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_ = {'monday':1 , 'tuesday':2 , 'wednesday':3 , 'thursday':4 , 'friday':5 , 'saturday':6 , 'sunday':7 , 'all':8}
    day = ''
    while day not in day_.keys():
        print('please enter the day')
        day = input().lower()
        if day not in day_.keys():
            print('sorry, i didnt understand that, please try again')

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    
    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        
        df = df[df['Month'] == month]

    
    if day != 'all':
        
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df[df['Month']].mode()
    print(f'most common month: {popular_month}')

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print(f'\nmost common day: {popular_day}')

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f'\nmost common start hour: {popular_hour}')

    print(f"\nThis took { (time.time() - start_time)} seconds")
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print(f'most common start station: {popular_start}')

    # display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print(f'\nmost common end station: {popular_end}')

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'].str.cat(df['End Station'], sep = ' to ')
    popular_combination = df['combination'].mode()[0]
    print(f'\nmost common combination: {popular_combination}')

    print(f"\nThis took {(time.time() - start_time)} seconds")
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    minute, second = divmod(total_time, 60)
    hour, minute = divmod(minute, 60)
    print(f'total travel time is {hour} hours, {minute} minutes, {second} seconds')

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    mins, sec = divmod(mean_time, 60)
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe average trip duration is {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe average trip duration is {mins} minutes and {sec} seconds.")



    print(f"\nThis took {(time.time() - start_time)} seconds")
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = pd.value_counts(df['User Type'])
    print(f'total users {user_types}')


    # Display counts of gender
    try:
        gender = pd.value_counts(df['Gender'])
        print(f'types of users by gender: {gender}')
    except:
        print('there is no gender')


    # Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f'earliest birth year: {earliest}')
        print(f'most recent birth year: {recent}')
        print(f'most common birth year: {common_year}')
    except:
        print('there is no birth year')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    
    RESPONSE_LIST = ['yes', 'no']
    response = ''
    counter = 0
    while response not in RESPONSE_LIST:
        print("\nDo you want to view the raw data?")
        response = input().lower()
        if response == "yes":
            print(df.head())
        elif response not in RESPONSE_LIST:
            print("\nsorry, i didnt understand that")

    while response == 'yes':
        print("Do you want to view more raw data?")
        counter += 5
        response = input().lower()
        if response == "yes":
             print(df[counter:counter+5])
        elif response != "yes":
             break

    print('-'*40)    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
