import pandas as pd
import numpy as np

from scispacy.abbreviation import AbbreviationDetector
from sklearn.metrics.pairwise import cosine_similarity

def semantic_similarity(nlp, x, y):
### returns cosine distance between x and y nlp embeddings
    x_vec = nlp(x).vector.reshape(1, -1)
    y_vec = nlp(y).vector.reshape(1, -1)

    return cosine_similarity(x_vec, y_vec)[0, 0]

def get_abbreviation_df(nlp, data, fields, skip_zero=False, skip_duplicate=True):
### finds abrv, its meaning and cosine similarity between abrv and meaning in data (DataFrame) fields (list)
### nlp - embedding dictionary (e.g. en_core_sci_lg)
### skip_zero - skip abbreviations without embeddings
### skip_duplicate - skip duplicate abbreviations
    abbreviation_pipe = AbbreviationDetector(nlp)
    nlp.add_pipe(abbreviation_pipe)
    n_dim = nlp("").vector.shape[0]
    abrv_set = set()

    rez = pd.DataFrame(columns = ["abrv", "meaning", "similarity"])

    for field in fields:
        for s in data[field]:
            if not pd.isna(s):
                doc = nlp(s)

                for abrv in doc._.abbreviations:
                    abrv_str = str(abrv)
                    if not (skip_zero and np.allclose(nlp(abrv_str).vector, np.zeros(n_dim))):
                        if not (skip_duplicate and abrv_str in abrv_set):
                            abrv_set.add(abrv_str)

                            meaning = str(abrv._.long_form)
                            sim = semantic_similarity(nlp, abrv_str, meaning)
                            rez = rez.append({"abrv": abrv_str, "meaning": meaning, "similarity": sim}, ignore_index=True)

    return rez







