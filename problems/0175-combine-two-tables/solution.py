"""Pandas solution"""

import pandas as pd


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    """Combine two tables with pd.merge"""
    return pd.merge(person, address, on="personId", how="left")[
        ["firstName", "lastName", "city", "state"]
    ]


def combine_two_tables_concat(
    person: pd.DataFrame, address: pd.DataFrame
) -> pd.DataFrame:
    """Combine two tables with pd.concat"""
    return (
        pd.concat(
            [
                person.set_index("personId"),
                address.set_index("personId"),
            ],
            axis=1,
            join="outer",
        )
        .dropna(axis=0, how="all", subset=["firstName", "lastName"])
        .reset_index()[["firstName", "lastName", "city", "state"]]
    )
