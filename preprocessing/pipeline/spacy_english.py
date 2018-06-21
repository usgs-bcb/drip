import pandas as pd
import spacy
import yaml
import os

# Fetch configuration information
env_vars = yaml.load(open('config.yaml').read())

english_ner_model = env_vars['english_ner_model']
GDD_OUTPUT = env_vars['candidate_dataframe']
output_directory = env_vars['output_directory']

# spacy
nlp = spacy.load(english_ner_model, disable=['tagger', 'textcat', 'parser'])

df = pd.read_csv(GDD_OUTPUT)


# Spacy EN NER and text
def process_passage(x):
    y = nlp(' '.join(eval(x)))
    return [i.label_ for i in y.ents], [i.text for i in y.ents]


df['spacy_ner'] = df['passage'].apply(process_passage)
df.to_csv(os.join(output_directory, 'processed_spacy_english.csv'))
