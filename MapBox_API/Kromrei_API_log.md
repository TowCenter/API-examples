# These are the curl requests I made:

curl "https://api.mapbox.com/geocoding/v5/mapbox.places/-99.133209,19.432608.json?types=poi.landmark&access_token=your_token_here"

curl "https://api.mapbox.com/directions/v5/mapbox/walking/-73.956878,40.801742;-73.876998,40.850684?access_token=your_token_here"

# This is the html I used to test the map:
```html
<html>
<body>

This is a map of New York City, centered on Central Park.

<img alt='static Mapbox map of the New York City area'
src='https://api.mapbox.com/styles/v1/mapbox/streets-v10/static/-73.968285,40.785091,9.67,0.00,0.00/1000x600@2x?access_token=sk.eyJ1Ijoia3JvbXJlaWciLCJhIjoiY2pkMXoxcndyMGs4aDJxcWR3dWZoMTludiJ9.gt5np7nljnnbf8rrVBTy_w'>

</body>
</html>
```
# Getting Latitude/Longitude:

A quick google search reveals the latitude longitude coordinates for a
given place. You will want to use the pair that represents the N/S and
E/W with positive or negative values, rather than N/S or E/W.
Additionally, you can right-click anywhere on a Google Map and select
"what's here?" on the menu to get latitude longitude.

![](./Kromrei_API_log_img1.png)

Choose the coordinates that are listed below, these are the coordinates
that will work with the MapBox API.

![](./Kromrei_API_log_img2.png)