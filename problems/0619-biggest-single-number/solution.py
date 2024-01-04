import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    val_counts = my_numbers.value_counts().to_frame().reset_index()
    max_val = val_counts[val_counts["count"] == 1][["num"]].max().to_frame(name="num")
    return max_val


def biggest_single_number2(my_numbers: pd.DataFrame) -> pd.DataFrame:
    # shorter, drops all duplicates and only keeps singular values
    return my_numbers.drop_duplicates(keep=False).max().to_frame(name="num")
