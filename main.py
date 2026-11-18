# Program that tells you where the ISS is and if you will be able to see it.
# 1. Get the current position of the ISS, from the Open Notify API
# 2. Get the user's location, using the geocoder package, which uses the IP address of the user to get their location.
# 3. Get users current timezone, using the datetime package.
# 4. Get what time sunset is based on the user's long and latitude, with the Astral package.
# 5. Determine if the ISS is overhead, by checking if the ISS is within 5 degrees of the user's latitude and longitude.
# 6. Compare the current time to the sunset time, see if the current time is after sunset.
# 7. If the ISS is overhead and it is after sunset, then the ISS is potentially visible to the user.
# 8. Print the results to the user, telling them if the ISS is potentially visible, or if it is overhead but not after sunset, or if it is after sunset but not overhead, or if it is not currently visible.
# 9. If the ISS is not overhead i would like to tell the user where the current position of the ISS is.

# packages needed: requests, geocoder, astral, geopy, datetime
import requests
import geocoder
from geopy.geocoders import Nominatim
from astral import Observer
from astral.sun import sunset
from datetime import datetime

# Get the user's location
user_location = geocoder.ip('me')
user_latitude = user_location.latlng[0]
user_longitude = user_location.latlng[1]

# Get the current time, in the user's timezone
current_time = datetime.now().astimezone()

# Using astral to get the sunset time, from users timezone, based on their longitude and latitude
observer = Observer(latitude=user_latitude, longitude=user_longitude)
sunset_time = sunset(observer, date=current_time.date()).astimezone()

# Get the current position of the ISS, from the Open Notify API
response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

# Extract the ISS longitude and latitude from the response data
iss_longitude = data['iss_position']['longitude']
iss_latitude = data['iss_position']['latitude']

# Convert coordinates into a city or town
geolocator = Nominatim(user_agent="iss_tracker")

iss_location = geolocator.reverse(
    f"{iss_latitude}, {iss_longitude}"
)

if iss_location is not None:
    address = iss_location.raw.get("address", {})

    city = (
        address.get("city")
        or address.get("town")
        or address.get("village")
        or "Unknown location"
    )
else:
    city = "Unknown location"

# Check whether the current time is later than sunset
is_after_sunset = current_time > sunset_time

# Check whether the ISS is within 5 degrees of the user's latitude and longitude
is_iss_overhead = (
    abs(float(iss_latitude) - user_latitude) < 5
    and abs(float(iss_longitude) - user_longitude) < 5
)

# The ISS is potentially visible if it is after sunset and overhead
is_iss_visible = is_after_sunset and is_iss_overhead

# Where the ISS is currently located.

# Print the results
if is_iss_visible:
    print("The ISS is potentially visible!")
elif is_iss_overhead:
    print("The ISS is nearby, but it is not after sunset.")
elif is_after_sunset:
    print("It is after sunset, but the ISS is not overhead.")
else:
    print("The ISS is not currently visible.")

# Print the current position of the ISS, and the city or town it is currently over, if it is over land.
if city == "Unknown location":
    print("The ISS is currently over the ocean.")
else:
    print(f"The ISS is currently near {city}.")
print(f"The ISS is currently located at {iss_latitude}, {iss_longitude}.")