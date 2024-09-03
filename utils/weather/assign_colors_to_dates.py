# app/views/weather/assign_colors_to_dates.py
def assign_colors_to_dates(weather_forecast, colors=None):
    """
    Assigns a color to each unique date in the weather forecast.

    :param weather_forecast: List of weather data, each containing a 'date' key.
    :param colors: List of colors to cycle through. Defaults to a predefined list if not provided.
    :return: A dictionary mapping each unique date to a color.
    """
    if colors is None:
        colors = ['#f0e5de', '#d9cfc1']  # Sand beige and soft taupe

    day_colors = {}
    day_counter = 0  # Initialize day counter

    for day in weather_forecast:
        date = day['date'].split(' ')[0]  # Extract the date part from datetime

        if date not in day_colors:
            # Assign color based on whether the day_counter is even or odd
            color = colors[day_counter % 2]
            day_colors[date] = color  # Assign color to the date
            day_counter += 1  # Increment the day counter only when a new date is encountered

    return day_colors

