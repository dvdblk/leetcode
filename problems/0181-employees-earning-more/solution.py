import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # self join on managerId
    df = pd.merge(employee, employee, left_on="managerId", right_on="id")
    # filter employees earning more than their managers
    df_employees = df[df["salary_x"] > df["salary_y"]]
    # return only the employee column
    return df_employees.rename(columns={"name_x": "Employee"})[["Employee"]]
