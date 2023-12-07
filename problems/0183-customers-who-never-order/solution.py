import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # left outer join
    df = pd.merge(customers, orders, left_on="id", right_on="customerId", how="left")
    # select rows where order id is null
    df = df[df["id_y"].isna()]
    # rename column
    df = df.rename(columns={"name": "Customers"})
    return df[["Customers"]]
