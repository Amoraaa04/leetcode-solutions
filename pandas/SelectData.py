import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    filtered = students[students['student_id'] == 101]
    return filtered.drop(columns=['student_id'])

# - My solution wasn't as efficient. I learned that it's better to use .loc (more efficient & cleaner)
# - Filters rows and selects columns in a single step
#
# students.loc[students['student_id'] == 101, ['name', 'age']]
