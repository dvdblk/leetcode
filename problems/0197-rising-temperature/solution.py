import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # Date to datetime
    weather["recordDate"] = pd.to_datetime(weather["recordDate"])

    # Sort by date
    weather.sort_values("recordDate", inplace=True)

    # Calculate previous day distance in days
    weather["prev_day_distance"] = (
        weather["recordDate"].shift(1) - weather["recordDate"]
    ).dt.days

    # Create yesterday's temp column
    weather["temperature_yesterday"] = weather["temperature"].shift(1)

    # Check if previous day distance is -1 and temp got higher
    return weather[
        (weather["prev_day_distance"] == -1)
        & (weather["temperature"] > weather["temperature_yesterday"])
    ][["id"]]
