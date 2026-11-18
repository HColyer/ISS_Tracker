
# ISS Tracker

A Python application that retrieves the International Space Station's (ISS) current position and compares it with the user's approximate location to assess whether the ISS may be visible.

## Features

- Retrieves the ISS's live latitude and longitude using an external API.
- Estimates the user's location using their IP address.
- Calculates local sunset using the Astral library.
- Compares the ISS's coordinates with the user's coordinates.
- Determines whether the ISS is potentially visible based on approximate proximity and sunset conditions.
- Uses reverse geocoding to identify a nearby city or town when possible.
- Displays the ISS's current geographical coordinates.

## Technologies Used

- Python
- Requests
- Geocoder
- Astral
- Geopy
- Open Notify API
- Nominatim / OpenStreetMap

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/HColyer/iss-tracker.git
   ```

2. Navigate into the project directory:

   ```bash
   cd iss-tracker
   ```

3. Create and activate a virtual environment (optional but recommended).

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   python main.py
   ```

## How It Works

The application retrieves the ISS's current coordinates and the user's approximate geographical location.

It then calculates the user's sunset time and uses Boolean conditions to determine whether the ISS is potentially visible.

If the ISS is not nearby, the application also displays its current coordinates and attempts to identify the geographical area.

## Limitations

- IP-based geolocation is approximate and may not identify the user's exact location.
- The five-degree coordinate comparison is a basic proximity check, not an accurate overhead calculation.
- Sunset and proximity alone cannot guarantee that the ISS is visible.
- Reverse geocoding may not identify a city or town when the ISS is over an ocean or remote area.

## Future Improvements

- Improve the ISS visibility calculation.
- Add more accurate timezone detection.
- Introduce improved error handling for external API requests.
- Explore AI integration to provide natural-language geographical descriptions.

## Author

Harry Colyer

GitHub: [HColyer](https://github.com/HColyer)
