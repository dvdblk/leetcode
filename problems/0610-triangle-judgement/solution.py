import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    x, y, z = triangle["x"], triangle["y"], triangle["z"]
    # triangle inequality
    tri_ineq = (x + y > z) & (x + z > y) & (y + z > x)
    # replace boolean with string
    triangle["triangle"] = tri_ineq.map({True: "Yes", False: "No"})
    return triangle