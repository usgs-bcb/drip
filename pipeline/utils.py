import yaml
import psycopg2
import requests
import spacy
import pandas as pd


def remap_sent(sent):
    """Remapping a sentence to a list of strings.

    Parameters
    ----------
    sent : string
    """
    return " ".join(sent)


def n_sents(idx, df):
    """Returns the surrounding sentences in rel to dataframe."""
    start = idx
    end = idx
    if idx > 0:
        start = idx - 1
    if idx < len(df):
        end = idx + 1
    return (start, end)


def n_upper(token, sentence):
    """Returns uppercase tokens surrounding term."""
    span = ""
    idx = sentence.split().index(token)
    while idx > 0:
        idx = idx - 1
        if sentence.split()[idx][0].isupper():
            if len(span) > 1:
                span = sentence.split()[idx] + " " + span
            else:
                span = span + sentence.split()[idx]
        else:
            return span
    return span


def sentence_elements(df, docid, sentid):
    sentence_df = df[(df["docid"] == docid) & (df["sentid"] == int(sentid))]
    return sentence_df


def rm_reference(sentence):
    """Cleans string sentence.

    Parameters
    ----------
    sentence : str
    """
    try:
        while "-LRB-" in sentence.split():
            if "-LRB-" in sentence.split() and "-RRB-" in sentence.split():
                # contains par
                start_idx = sentence.split().index("-LRB-")
                end_idx = sentence.split().index("-RRB-")

                sentence = (
                    sentence.split()[:start_idx]
                    + sentence.split()[end_idx + 1 :]
                )
        return remap_sent(sentence)
    except:
        return sentence


def connect_db():
    """Quickly connect to a database.

    Note this expects a local yaml file to contain credentials
    passed into the connector.

    Returns
    -------
    Pandas Dataframe
    """
    with open("./config.yml", "r") as f:
        conf = yaml.load(f)

    conn = psycopg2.connect(
        dbname=conf["postgres"]["database"],
        user=conf["postgres"]["user"],
        host=conf["postgres"]["host"],
        port=conf["postgres"]["port"],
        password=conf["postgres"]["password"],
    )
    cursor = conn.cursor()

    df = pd.read_sql_query(
        "select docid, sentid, wordidx, words, poses, ners from sentences_nlp352;",
        con=conn,
    )
    print("Sentences: %s" % len(df))
    return df


# Loading related data
def get_drip_resources(
    URL="https://beta-gc2.datadistillery.org/api/v1/sql/bcb?q=select * from drip.dripdams"
):
    """Export of known dam removals from data distillery.

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
            raise Exception("Data Distillery URL returning: %s", r.status_code)
    except Exception as e:
        raise Exception(e)


def get_dams():
    # Load Data Distillery dam data
    dams = pd.DataFrame(
        [i["properties"] for i in get_drip_resources()["features"]]
    )
    # Cleaned name list
    # Rm river/dam and related words
    dams["name"] = dams["dam_name"].str.replace("Unknown", "")
    dams["name"] = dams["name"].dropna()
    dams["name"] = (
        dams["dam_name"]
        .str.replace("Dam", "")
        .replace("River", "")
        .replace("River)", "")
        .replace("dam", "")
    )
    return dams


def custom_ner(
    passage,
    ner=spacy.load(
        "/Users/bserna/Developer/drip-knowledge-extraction/NER/dam-ner-spacy-v2"
    ),
):
    """Fuction to identify if the custom ner matches an item within a passage.
    
    Parameters
    ----------
    passage : string
        Sentence 
        
    Returns
    -------
    list
        Matching Dam NER tokens

    """
    matches = []
    doc = ner(passage)
    for ent in doc.ents:
        if ent.label_ == "Dam":
            matches.append(ent.text)

    if len(matches) >= 1:
        return matches


def removal_identifiers_present(passage, nlp):
    """Function to process when certain identifing flags are within the given passage.
    
    Parameters
    ----------
    passage : string
        Sentence
        
    Returns
    -------
    bool
    """
    doc = nlp(passage)
    stemming_words = ["remove", "removal", "breech", "destroy"]
    for token in doc:
        if token.lemma_ in stemming_words:
            return True


def removal_identifiers_found(passage, nlp):
    """Function to process when certain identifing flags are within the given passage.

    Parameters
    ----------
    passage : string
        Sentence

    Returns
    -------
    bool and terms found
    """
    found = []
    doc = nlp(passage)
    stemming_words = ["remove", "removal", "breech", "destroy"]
    for token in doc:
        if token.lemma_ in stemming_words:
            found.append(token.lemma_)
    return found


def damrm_date_present(core_nlp_ner, spacy_ner):
    """Function to identify if a date was found.

    Parameters
    ----------

    core_nlp_ner: list
        Returned from geodeepdive output

    spacy_ner: spacy model of the entities

    Output
    ------

    True if date objects found in both CoreNLP and Spacy
    """
    if "DATE" in core_nlp_ner and "DATE" in [i.label_ for i in spacy_ner.ents]:
        return True


def bidaf_year_query(dam, passage, removal_term="removed", BIDAF_URL='http://0.0.0.0:1995/submit'):
    """Function to interface with bidaf.

    Parameters
    ----------
    dam
        The in-context dam

    passage
        Sentence or span of text to use as the context
    """
    question = "When was %s %s?" % dam, removal_term
    payload = {"context": passage, "question": question}

    return requests.post(BIDAF_URL, payload).json()["answers"]
