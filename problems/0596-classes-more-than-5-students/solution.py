import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    counted = courses.groupby(["class"]).agg(n_students=("student", "count"))
    result = counted[counted["n_students"] >= 5].reset_index()
    return result[["class"]]
