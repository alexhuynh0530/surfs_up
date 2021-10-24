# surfs_up

# An Analysis of Weather Data using SQLite, SQLAlchemy, and Flask

## Overview of Project

### Purpose

This is an anlayis of weather data using:
- SQL - A version of SQL that lives on a computer or phone
- SQLAlchemy - A query tool for SQLite
- Flasl - A web framework that uses Python to build web pages

Use case:
W. Avy is a potential investor of our "Surf 'n Shake" shop wants more information about temperature trends before opening the surf shop. Specifically, he wants temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

## Results

### Determine the Summary Statistics for June and December

Using Python, Pandas functions and methods, and SQLAlchemy, we filter the date column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures for the month of June and December. We then convert those temperatures to a list, create a DataFrame from the list, and generate the summary statistics.

![SurfsUp_Challenge.ipynb](https://github.com/alexhuynh0530/surfs_up/blob/main/SurfsUp_Challenge.ipynb)

#### June Temp Stats
![june_temp.png](https://github.com/alexhuynh0530/surfs_up/blob/main/Resources/june_temp.png)

#### December Temp Stats
![dec_temp.png](https://github.com/alexhuynh0530/surfs_up/blob/main/Resources/dec_temp.png)

- Looking at the temperature data from June and December, the average temp are relatively the same with June at 74.9 and December at 71.04, indicating that the surf and ice cream shop business could be sustainable year-round
- Looking at the minimum temperatures from June and December, you see that December gets as low as 56 with June getting as low as 64. Depending on temperature preference, some days in December may not be ideal for business on the colder days versus the colder days in June.
- You can see that December has a greater standard deviation meaning the temperatures are a bit more dispersed in relation to the mean or average. This is important to consider, because even with the December average temperature is 71.04, there is a wide spread that may include more colder temperatures on certain dates which are not ideal for business.


## Summary

In summary, 
