import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    """map"""
    salary["sex"] = salary["sex"].map({"f": "m", "m": "f"})
    return salary

def swap_salary2(salary: pd.DataFrame) -> pd.DataFrame:
    """replace"""
    return salary.replace({"f": "m", "m": "f"})

def swap_salary3(salary: pd.DataFrame) -> pd.DataFrame:
    """apply"""
    def swap(sex):
        return "m" if sex == "f" else "f"

    salary["sex"] = salary["sex"].apply(swap)
    return salary
