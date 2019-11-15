Data Description

In order to accomplish this goal, latitudes and longitudes of the capital cities of all countries in the world are required. The "simplemaps.com" offers a simple, accurate and up-to-date database of the world's cities and their locations. From this data, I need to select the capital cities and using their latitude and longitude values, I need to explore the venues with "art" section around these cities by utilizing Foursquare API.

The "simplemap" data contains city name, corresponding latitude, longitude and country name along with many other features for all cities in the world. I only use the features that I mentioned in this data and then filtered the capital cities for each country. After cleaning the data I have 225 countries with 225 capital cities.

Then I used the acquired location data to explore the nearby art venues from the Foursquare API. Using the "explore" option, I look for top 25 art venues in 10 km radius for each city center and I get "Venue", "Venue Latitude", "Venue Longitude" and "Venue Category" columns with 3316 row in total.
