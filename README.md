## Date created
July 2019

## Explore US Bikeshare Data

## Description
### Project Submission:
In this project, I have written Python code to import US bike share data and answer interesting questions about it by computing descriptive statistics. I have written a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

### Bike Share Data:
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

This project uses data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns.

Data from Chicago, New York City, and Washington, DC was used in this project.

### Data Structure:

Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (in seconds - e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
- Gender
- Birth Year

This project computes the following statistics:

### #1: Popular times of travel (i.e., occurs most often in the start time):
- most common month
- most common day of week
- most common hour of day

### #2: Popular stations and trip:
- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

### #3: Trip duration:
- total travel time
- average travel time

### #4: User info:
- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)


## Files used
- chicago.csv
- new_york_city.csv
- washington.csv

## Credits
This project was completed for Udacity's Programming for Data Science Nanodegree program. Project template and instructions provided by [Udacity] (https://www.udacity.com).
