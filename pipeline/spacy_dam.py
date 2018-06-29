import pandas as pd
import spacy
import yaml
import os

# Fetch configuration information
env_vars = yaml.load(open("/Users/bserna/airflow/config.yaml").read())

SPACY_DAM_MODEL_PKG = env_vars["dam_ner_model"]
GDD_OUTPUT = env_vars["candidate_dataframe"]
OUTPUT_DIRECTORY = env_vars["output_directory"]


# spacy
dam_ner = spacy.load(
    SPACY_DAM_MODEL_PKG, disable=["tagger", "textcat", "parser"]
)

df = pd.read_csv(GDD_OUTPUT).iloc[:1000]


def process_passage(x):
    y = dam_ner(" ".join(eval(x)))
    return [i.label_ for i in y.ents], [i.text for i in y.ents]


df["spacy_dam"] = df["passage"].apply(process_passage)

df.to_csv(os.path.join(OUTPUT_DIRECTORY, "processed_spacy_custom_dam.csv"))
