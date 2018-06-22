import pandas as pd
import spacy
import yaml
import os

# Fetch configuration information
env_vars = yaml.load(open("config.yaml").read())

dam_ner_model = env_vars["dam_ner_model"]
GDD_OUTPUT = env_vars["candidate_dataframe"]
output_directory = env_vars["output_directory"]


# spacy
dam_ner = spacy.load(dam_ner_model, disable=["tagger", "textcat", "parser"])

df = pd.read_csv(GDD_OUTPUT).iloc[:10000]


def process_passage(x):
    """Custom Spacy Dam NER."""
    y = dam_ner(" ".join(eval(x)))
    return [i.label_ for i in y.ents], [i.text for i in y.ents]


df["spacy_dam"] = df["passage"].apply(process_passage)

df.to_csv(os.path.join(output_directory, "processed_spacy_custom_dam.csv"))
