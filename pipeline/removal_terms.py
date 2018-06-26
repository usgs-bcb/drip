import pandas as pd
import spacy
from utils import removal_identifiers_found
import yaml
import os

# Fetch configuration information
env_vars = yaml.load(open("config.yaml").read())

GDD_OUTPUT = env_vars["candidate_dataframe"]
OUTPUT_DIRECTORY = env_vars["output_directory"]
SPACY_EN_MODEL_PKG = env_vars["english_ner_model"]

# spacy
nlp = spacy.load(SPACY_EN_MODEL_PKG, disable=["tagger", "textcat", "parser"])

df = pd.read_csv(OUTPUT_DIRECTORY).iloc[:10000]


# Removal terms
def rm_terms(x):
    y = " ".join(eval(x))
    # Returning the found lemmas as a list
    return removal_identifiers_found(y, nlp)


df["removal_terms"] = df["passage"].apply(rm_terms)

df.to_csv(os.path.join(OUTPUT_DIRECTORY, "processed_step2_rm_terms.csv"))
