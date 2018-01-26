import pickle
import pandas as pd
import textacy


def build_document(df):
    '''
    Rebuilding a representation of a document from the
    sentences_nlp352 format.

    Parameters
    ----------
    df : pandas dataframe
    '''
    # Find unique documents
    document_ids = pd.Series(df.docid.unique())

    for docid in document_ids[:1]:
        doc = df[df.docid==docid]['word']
        cleaned_doc = textacy.preprocess_text(' '.join(doc.str.cat().replace('{', '').replace('}', '').replace('.', ' . ').split(',')))

        return cleaned_doc.replace('" "', '')


def classify_doc(doc):
    '''
    Loading a pretrained document classifier to predict
    a class for the given text. Options are abiotic, 
    biotic, and abiotic&biotic. 

    Parameters
    ----------
    doc : string
    '''
    # Load scikit learn model
    clf = pickle.load(open('../document-classification/random_forest_classifier.sklearn', 'rb'))
    # Load previous tfidf representation
    load_tfidf = pickle.load(open('../document-classification/tfidf.sklearn', 'rb'))
    print('Resources Loaded')

    # Need to build a document representation here
    # pre-process
    tfidf = load_tfidf.transform([build_document(doc)])
    prediction = clf.predict(tfidf)
    if prediction == 0:
        # output to file
        with open('./output/classifications.tsv', 'w') as f:
            f.write('Filename')
            f.write('\t')
            f.write('Abiotic')
    if prediction == 1:
        # return {'Classification': 'Biotic', 'File': 'insert doc name here'}
        # output to file
        with open('./output/classifications.tsv', 'w') as f:
            f.write('Filename')
            f.write('\t')
            f.write('Biotic')
    if prediction == 2:
        # return {'Classification': 'Biotic & Abiotic', 'File': 'insert doc name here'}
        # output to file
        with open('./output/classifications.tsv', 'w') as f:
            f.write('Filename')
            f.write('\t')
            f.write('Biotic & Abiotic')