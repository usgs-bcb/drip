""" Utility functions for app """
import requests
import pandas as pd


# Loading related data
def get_drip_resources(URL='https://beta-gc2.datadistillery.org/api/v1/sql/bcb?q=select * from drip.dripdams'):
    """Export of known dam removals from data distillery

    Parameters
    ----------
    URL : str
        Built query for GC2.
    """
    try:
        r = requests.get(URL)
        if r.status_code == 200:
            return r.json()
        else:
            raise Exception('Data Distillery URL returning: %s', r.status_code)
    except Exception as e:
        raise Exception(e)


def load_nlp352(file='./data/sentences_nlp352'):
    """Return a pandas dataframe from GDD export

    Notes
    -----
    Get a list of document identifiers
    >>> document_ids = pd.Series(df.docid.unique())

    Filter for an individual
    >>> df[df.docid=='5705014ccf58f18a4c0d6d61']
    """
    df = pd.read_csv(file, sep='\t', lineterminator='\n', header=None)
    df.columns = ['docid', 'sentid', 'wordidx', 'word', 'poses', 'ners', 'lemma', 'dep_paths', 'dep_parents']
    return df