import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.groupby(["player_id"]).agg(
        {"player_id": "first", "event_date": min}
    )
    activity.rename(columns={"event_date": "first_login"}, inplace=True)
    return activity
