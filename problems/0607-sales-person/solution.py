import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # 3 way join
    merged = company.merge(orders, on="com_id").merge(sales_person, on="sales_id", how="outer")
    # get unique names of people that have a red order
    has_red_orders = merged[merged["name_x"] == "RED"][["name_y"]].drop_duplicates()
    # return the complement of the names
    return sales_person[~sales_person["name"].isin(has_red_orders["name_y"])][["name"]]

