import re
import pandas as pd
import datetime

data = pd.read_csv('data/abbreviation_dict.csv', sep='\t')
rez_df = pd.DataFrame(columns = ["abrv", "meaning", "similarity"])

print("start time: ", datetime.datetime.now().strftime('%H:%M:%S'))

i = 0
while i < data.shape[0]:
    abrv = data["abrv"].iloc[i]
    if not pd.isna(abrv):
        if not re.search("[^a-zA-z0-9]", abrv) and not abrv.isnumeric() and len(abrv) > 1:
            rez_df = rez_df.append({"abrv": data["abrv"].iloc[i], "meaning": data["meaning"].iloc[i], "similarity": data["similarity"].iloc[i]}, ignore_index=True)

    if i % 100 == 0:
        print(i)
    i += 1

rez_df.to_csv("data/abbreviation_dict_clean.csv", sep='\t', index=False)

print("end time: ", datetime.datetime.now().strftime('%H:%M:%S'))

