import time
import pandas as pd
import numpy as np


‫#‬ to do 
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Chose the city (chicago, new york city, washington)").lower()
    while city.lower() not in ['chicago','new york city','washington']:
        print(city + " is not valid, try again!")
        city = input("Chose the city (chicago, new york city, washington)").lower()#ignore upper case 
        
    print("User input city is " + city)
    # TO DO: get user input for month (all, january, february, ... , june)
     
    month = input("Chose the month (january, february, march, april, may, june or all)").lower() #ignore upper case
    while month.lower() not in ['all','january','february','march','april','may','june']:
        print(month + " is not valid, try again!")
        month = input("Chose the month (january, february, march, april, may, june or all)").lower() #ignore upper case 
        
    print("User input month is " + month)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Chose the day (all, saturday, sunday, monday, tuesday, wednesday, thursday or friday)").lower() #ignore upper case
    while day.lower() not in ['all','saturday','sunday','monday','tuesday','wednesday','thursday','friday']:
        print(day + " is not valid, try again!")
        day = input("Chose the day (all, saturday, sunday, monday, tuesday, wednesday, thursday or friday)").lower() #ignore upper case 
        
    print("User input day is " + day)


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

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('Most Frequent Month :', common_month)

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.strftime('%A')
    common_day = df['day'].mode()[0]
    print('Most Frequent day of week :', common_day)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour :', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station is:', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station is:', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    startEnd_combination = df['End Station'].mode()[0] + df['Start Station'].mode()[0] 
    print('Most frequent combination of start station and end station trip is :', startEnd_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total Travel Time is :', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time is :', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types is :\n', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('Counts of Gender is :\n', gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        print('Earliest year of birth is :', earliest)
        most_recent = df['Birth Year'].max()
        print('Most Recent Year of birth is :', most_recent)
        most_common = df['Birth Year'].mode()
        print('Most Common year of birth is :', most_common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        startRow = 0 
        endRow = 5
        
        while True:
            rowData = input('\nWould you like to see some of row data? Enter yes or no.\n')
            if rowData.lower() == 'yes':
                print(df.iloc[startRow:endRow]) 
                startRow +=5
                endRow +=5
            else: break 

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            


if __name__ == "__main__":
	main()
