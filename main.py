# Python file to extract the missing postcodes in Airbnb Dataframe, using Geopy.
# Importing numpy as well for the vectorize() method for faster runtime.
# Original Dataframe: http://insideairbnb.com/get-the-data/

# Runtime of this program with the size of the data is excessive with Nominatim, for possible faster execution
# Other geolocators can be considered, such as Google's own geolocator.

import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.point import Point
# openpyxl is needed only once, to be able to open the .xlsx file.
# If you would like to use the provided .csv, this package is not needed.
import openpyxl

geolocator = Nominatim(user_agent="test")

# Read listings.csv into MS Excel for further customization, which was provided as input below.
# Code can be replaced with df = pd.read_csv(listings.csv)
df = pd.read_excel("data/Final.xlsx", sheet_name="listings")


# Latitudes and Longitudes are present in .csv file, using reverse() method to find the postcodes.
def reverse_geocoding(lat, lon):
    # Some data might have errors (missing or faulty longitude and latitude), these need to be handled.
    try:
        location = geolocator.reverse(Point(lat, lon))
        # Below row returns all the available data of the locations, but we don't need all of them for this practice .
        # return location.raw['display_name']
        return location.raw['address']['postcode']
    # The faulty ones will return Null, which we can filter out as needed
    except KeyError:
        return None


# Extracting the latitudes and longitudes to a new output file, as it helps us match the postcodes with the Dataframe.
df = pd.DataFrame({
    'Latitude': df['latitude'],
    'Longitude': df['longitude']
})

df['Postcode'] = np.vectorize(reverse_geocoding)(df['Latitude'], df['Longitude'])
df.to_csv("postcodes.csv")
