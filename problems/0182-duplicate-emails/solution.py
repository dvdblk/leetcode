import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # find all duplicate rows
    df = person[person.duplicated(["email"], keep=False)]
    # only keep one of the duplicate rows
    df = df.drop_duplicates("email")
    # rename
    df = df.rename(columns={"email": "Email"})
    return df[["Email"]]
