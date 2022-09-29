# AirbnbAnalysis_Denmark
Data analysis with Python, SQL, and Tableau of Airbnb data in Denmark.

All data provided on: http://insideairbnb.com/get-the-data/
Files used: listings.csv.gz and calendar.csv.gz from Denmark
All data revolves around Copenhagen only

Problem:

- When and where is it the most economic to rent on Airbnb in Copenhagen?
- What are the revenue expectation considering multiple metrics (location, dates, host status, bedrooms etc.)

Solution:

- Collecting data
- Cleaning data using MS Excel, MS Access or similar (MySql, PostgreSQL, SSMS, Azure etc.)
- Exploring more data with Python's Geopy library
- Gathering and visalizing data in Tableau

Problems faced and what I've learned:

- After reading in the listing.csv file into excel, multiple data shared the same cell, which needed to be divided into further cells.
- calendar.csv has more than 4.5 million rows, that MS Excel can not handle, thus SQL database was needed.


