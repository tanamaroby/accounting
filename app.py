# Imports
from re import M
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
category_mapping = {
    'A': 'Assets',
    'L': 'Liabilities',
    'OE': 'Equity'
}

for row in df_array:
    is_debit = math.isnan(row[3])
    value = row[2] if is_debit else row[3]
    time = previous_time if pd.isnull(row[0]) else row[0]
    input_string = row[1].split()
    category = category_mapping[input_string[-1][1:-1]]
    name = ' '.join(input_string[0:-1])
    data.store_journal(name, category, is_debit, value, time)
    previous_time = time

data.print_journal()

