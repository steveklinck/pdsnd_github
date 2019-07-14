import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv',
              'new york': 'new_york_city.csv' }

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
    while True:
        city = input("Which city would you like to analyze? Type New York, Chicago, or Washington\n")
        city = city.lower()
        if city not in ('new york', 'new york city', 'chicago', 'washington'):
            print('Please enter either New York, Chicago, or Washington as your city')
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month would you like to filter by? You can select January, February, March, April, May, June, or "none"\n')
        month = month.lower()
        if month not in ('january','february','march','april','may','june','none'):
            print('Please enter a valid month, or type "none"')
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Would you like to filter by day (enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday)? If not, type "none"\n')
        day = day.lower()
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'none'):
            print('Please enter a valid day or type "none"')
            continue
        else:
            break


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

# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

      # filter by month if applicable
    if month != 'none':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
 # filter by day of week if applicable
    if day != 'none':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    common_month_dict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June'}
    common_hour_dict = {0:'12 am', 1: '1 am', 2:'2 am', 3:'3 am', 4:'4 am', 5:'5 am', 6:'6 am', 7:'7 am', 8:'8 am', 9:'9 am', 10:'10 am', 11:'11 am', 12:'12 pm', 13:'1 pm', 14:'2 pm', 15:'3 pm', 16:'4 pm', 17:'5 pm', 18:'6 pm', 19:'7 pm', 20:'8 pm', 21:'9 pm', 22:'10 pm', 23:'11 pm'}

    print('\nCurrently Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month_dict[common_month])

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day:', common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common hour:', common_hour_dict[common_hour])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCurrently Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('\nMost commonly used start station:', start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('\nMost commonly used end station:', end_station)


    freq_combination = df[['Start Station', 'End Station']].mode().loc[0]
    concat_combo = freq_combination[0] + " & " + freq_combination[1]
    print('\nMost commonly used combination of start and end station:',concat_combo)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCurrently Calculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time/86400, " Days")

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCurrently Calculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # Display counts of gender
    try:
      gender_count = df['Gender'].value_counts()
      print('\nGender Count:\n', gender_count)
    except:
      print("\nGender Count: No gender data available")

    # Display earliest, most recent, and most common year of birth
    try:
      earliest_yob = int(df['Birth Year'].min())
      print('\nEarliest year of birth:', earliest_yob)
    except:
      print("\nEarliest year of birth: No data available")

    try:
      most_recent_yob = int(df['Birth Year'].max())
      print('\nMost recent year of birth:', most_recent_yob)
    except:
      print("\nMost recent year of birth: No data available.")

    try:
      most_common_yob = int(df['Birth Year'].value_counts().idxmax())
      print('\nMost common year of birth:', most_common_yob)
    except:
      print("\nMost common year of birth: No data available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_rows(df):
        x = 0
        while True:
            display_stats = input("Would you like to load 5 rows of individual trip data? Please enter yes or no\n")
            display_stats = display_stats.lower()
            if display_stats == 'yes':
                print(df[x : x +5])
                x = x + 5
                print('\n')
                continue
            else:
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_rows(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
