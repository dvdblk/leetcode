import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Sort by ID
    person.sort_values("id", inplace=True)
    # Remove duplicate emails, keep first
    person.drop_duplicates(subset="email", keep="first", inplace=True)
