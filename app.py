# Imports
import pandas as pd
import math

# Self-defined classes
from model.journal import journal

# Worksheet
df = pd.read_excel('worksheet.xlsx', na_values=0)

df_array = df.to_numpy()

# Data
data = journal()
previous_time = None

for row in df_array:
    is_debit = math.isnan(row[4])
    value = row[3] if is_debit else row[4]
    time = previous_time if pd.isnull(row[0]) else row[0]
    data.store_journal(row[1], row[2], is_debit, value, time)
    previous_time = time

data.print_journal()

