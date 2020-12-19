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
    while True:
        city= input('Please, which city would you like to explore from these three cities(chicago, new york city, washington)?\n').lower().strip()
        if city in CITY_DATA.keys():
            break
        else:
            print('Please enter a correct name of city!')




    # get user input for month (all, january, february, ... , june)
    while True:
        month= input('Please choose month, from January to June, to filter by or choose all?\n').lower().strip()
        month_names= ['january', 'february', 'march', 'april', 'may', 'june','all']
        if month in month_names:
            break
        else:
            print('Please re-enter correct name of month!')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input('which day of week would you like to filter by,or all?\n').title().strip()
        day_name= ['Sunday','Monday','Tuesday','Wendesday','Thursday','Friday','Saturday','All']
        if day in day_name:
            break
        else:
            print('Please re-enter correct name of day')

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
    df=pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        month_names= ['January', 'february', 'march', 'april', 'may', 'june']
        month = month_names.index(month) + 1

        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # display the most common month
    most_common_month=df['month'].mode()[0]
    print('The most common month is',most_common_month)

    # display the most common day of week

    most_common_DOW=df['day_of_week'].mode()[0]
    print('The most common day of week is',most_common_DOW)
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    most_common_hour=df['hour'].mode()[0]
    print('The most common start hour is',most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_startstation= df['Start Station'].mode()[0]
    print('The most common Start Stastaion is',most_common_startstation)

    # display most commonly used end station
    most_common_endstation= df['End Station'].mode()[0]
    print('The most common End Station is',most_common_endstation)

    # display most frequent combination of start station and end station trip
    most_frq_SandE_station=(df['Start Station']+df['End Station']).mode()[0]
    print('The most common trip is',most_frq_SandE_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('The total travel time is',total_travel_time)

    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('The avarge travel time is',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    try:
        df['Gender']=df['Gender'].dropna(axis=0)
        count_of_gender=df['Gender'].value_counts()
        print(count_of_gender)
    except:
        print('There is no data for gender in Washington' )

    # Display earliest, most recent, and most common year of birth
    try:
        df['Birth Year']=df['Birth Year'].dropna(axis=0)
        earlist_year=df['Birth Year'].min()
        most_recent_year=df['Birth Year'].max()
        most_common_year=df['Birth Year'].mode()[0]
        print('The earliest year of birth is',earlist_year)
        print('The most recent year of birth is',most_recent_year)
        print('The most common year of birth is',most_common_year)
    except:
        print('There is no data for year of birth in Washington')
    finally:
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def segement_data(df):
    """Display rows of raw data upon the request of user"""
    ask=input('Would you like to see raw data? Enter yes or no.\n').lower().strip()
    while True:
        if ask != 'yes':
            break
        else:
            while True:
                try:
                    rows=int(input('How many rows would you like to see? Please enter a number\n'))
                    print(df.head(rows))
                    ask=input('Would you like to see more raw data? Enter yes or no.\n')
                    break
                except:
                    print('Oops! it look like that you did not enter a number,\n')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        segement_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
