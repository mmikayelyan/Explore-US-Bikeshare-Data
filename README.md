# Explore-US-Bikeshare-Data
A Python project using pandas to explore bikeshare data.
# Project Overview
In this project, I made use of Python to explore data related to bike share systems for three major cities in the United States - Chicago, New York City, and Washington. I have written code to import the data and answer interesting questions about it by computing descriptive statistics. I have also written a script that takes in raw input to create an interactive experience in the jupter notebook to present these statistics.
# The Datasets
I used datasets provided by [Motivate](https://motivateco.com/), a bike share system provider in the US, containing randomly selected data for the first six months of 2017 for all three cities:

- Start Time 
- End Time 
- Trip Duration 
- Start Station 
- End Station 
- User Type 

The Chicago and New York City files also have the following two columns:

- Gender
- Birth Year

# Statistics Computed
I've written code to provide the following information:

- What month occurs most often in the start time?
- What day of the week (Monday, Tuesday, etc.) occurs most often in the start time? 
- What hour of the day occurs most often in the start time?
- What is the total trip duration and average trip duration?
- What is the most frequently used start station and most frequently used end station?
- What is the most common trip (i.e., the combination of start station and end station that occurs the most often)?
- What are the counts of each user type?
- What are the counts of gender?
- What is the earliest birth year (when the oldest person was born), most recent birth year, and most common birth year?


# The Interactive Experience
The program takes user input for the city (e.g. Chicago), month for which the user wants to view data (e.g. January; also includes an 'all' option), and day for which the user wants to view data (e.g. Monday; also includes an 'all' option).

Upon receiving the user input, it goes ahead and asks the user if they want to view the raw data (5 rows of data initially) or not. Following the input received, the program prints the details. Finally, the user is prompted with the choice of restarting the program or not.

# Requirements

* Language: Python 3.6 or above
* Libraries: pandas, numpy, time

# Get started with the project

Use the bikeshare.py to run the program in the Jupyter Notebook.

# Project Data

* chicago.csv - Stored in the data folder, the chicago.csv file is the dataset containing all bikeshare information for the city of Chicago provided by Udacity.

* new_york_city.csv - Dataset containing all bikeshare information for the city of New York provided by Udacity.

* washington.csv - Dataset containing all bikeshare information for the city of Washington provided by Udacity. Note: This does not include the 'Gender' or 'Birth Year' data.

# Author

 * [Manuk Mikayelyan](https://github.com/mmikayelyan) - Sole author for this program.
 
 # Acknowledgements

* [Udacity](https://udacity.com) - Udacity's Data Analyst Nanodegree program and [Masterschool](https://www.masterschool.com/) instructors were extremely helpful while I was pursuing this project.
* [stackoverflow](https://stackoverflow.com/questions/28189442/datetime-current-year-and-month-in-python#:~:text=import%20datetime%3B%20today%20%3D%20str(,and%20year%20in%20integer%20format
) - Datetime current year and month in Python
* [datatofish](https://datatofish.com/substring-pandas-dataframe/) - Select Rows Containing a Substring in Pandas DataFrame
* [stackoverflow](https://stackoverflow.com/questions/52458085/how-to-use-str-startswith-for-multiple-columns) - how to use str.startswith for multiple columns?
* [pandas docs](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.startswith.html) - Test if the start of each string element matches a pattern
