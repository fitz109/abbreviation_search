import pandas as pd
import en_core_sci_lg
import datetime
from abbreviation_search import get_abbreviation_df

nlp = en_core_sci_lg.load()
data = pd.read_csv('data/data.csv', sep='\t')
# data = data[:10] # get partial data
fields = ["abstract"]

print("start time: ", datetime.datetime.now().strftime('%H:%M:%S'))

df = get_abbreviation_df(nlp, data, fields, skip_zero=True, skip_duplicate=True)
df.to_csv('data/abbreviation_dict.csv', sep='\t', index=False)

print("end time: ", datetime.datetime.now().strftime('%H:%M:%S'))
