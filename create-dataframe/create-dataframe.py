import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    column_names = ["student_id", "age"]
    df = pd.DataFrame(student_data, columns=column_names)
    return df

print(createDataframe([[1,15],[2,11],[3,11],[4,20]]))