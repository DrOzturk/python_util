import pandas as pd

#usage: pass which cols has frozensets or any other objects serialized as stings in
#  serialized_cols param as a list of strings.
#  This will read from filepath_or_buffer first and then deserialize objects in those
#  columns.
def read_csv_improved(filepath_or_buffer, serialized_cols=[]):
    df = pd.read_csv(filepath_or_buffer)
    for col in serialized_cols:
        df.loc[:,col] = df.loc[:,col].map(eval)
    return df

pd.read_csv_improved = read_csv_improved

# def to_csv_improved(self,filename):
#     self.to_csv(filename)
#     print("saved to csv")

#pd.DataFrame.to_csv_improved = to_csv_improved