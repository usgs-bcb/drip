"""
Text mining application

CLI options:
    -classify
    -gdd
    -local

Local file input: burroughs.txt (not included)
GDD file input: sentences_nlp352
"""
import pandas as pd
import textacy
from sys import argv
import spacy
from utils import get_drip_resources, load_nlp352
from document_classifier import classify_doc
from extractors import find_dam_candidate_phrases, filter_candidate_phrases


if __name__ == '__main__':
    nlp = spacy.load('en')
    # Load Data Distillery dam data
    dams = pd.DataFrame([i['properties'] for i in get_drip_resources()['features']])
    # Cleaned name list
    # Rm river/dam and related words
    dams['name'] = dams['dam_name'].str.replace('Dam', '').replace('River', '').replace('River)', '').replace('dam', '')

    # Save output
    save_phrases = []
    save_names = []
    save_doc = []

    # CLI option
    if '-classify' in argv:
        df = load_nlp352()  # load geodeepdive data
        classify_doc(df)  # output in output dir
    if '-localfile' in argv:
        # Sample document from PDFtoText
        with open('./data/burroughs.txt', 'r') as f:
            file = f.read()
        doc = textacy.preprocess_text(file, fix_unicode=True).replace('\n', ' ')

        # Example processing
        doc_sents = doc.split('.')  # Separate by sentences
        print('Sentences: %s' % len(doc_sents))
        candidate_phrases = find_dam_candidate_phrases(doc_sents[:], ' dam')
        print('Candidate sentences: %s' % (len(candidate_phrases)))

        # Full run on doc
        for i in candidate_phrases:
            rslts = filter_candidate_phrases(i, nlp, dams)
            if len(rslts) != 0:
                for dam in filter(None, dams['dam_name']):
                    if dam in ' '.join(rslts):
                        save_names.append(dam)
                        save_phrases.append(' '.join(rslts))
                        print('Matched: ', dam)
                        print(rslts)
                        print('====================================')
    if '-gdd' in argv:
        df = load_nlp352()
        # preprocessing (single document 0)
        document_ids = pd.Series(df.docid.unique())

        # All documents 
        try:
            for idx, docid in enumerate(df['docid']):
                doc = df[df.docid == document_ids[idx]]['word']
                cleaned_document = textacy.preprocess_text(' '.join(doc.str.cat().replace('{', '').replace('}', '').replace('.', ' . ').split(',')))

                candidate_phrases = find_dam_candidate_phrases(cleaned_document.split('.'), ' dam')
                print('Candidate sentences: %s' % (len(candidate_phrases)))

                # Full run on doc
                for i in candidate_phrases:
                    rslts = filter_candidate_phrases(i, nlp, dams)
                    if len(rslts) != 0:
                        for dam in filter(None, dams['dam_name']):
                            if dam in ' '.join(rslts):
                                save_names.append(dam)
                                save_phrases.append(' '.join(rslts))
                                save_doc.append(docid)
                                print('Matched: ', dam)
                                print('Document: ', docid)
                                print(rslts)
                                print('====================================')
            # output to file
            with open('./output/results.tsv', 'w') as f:
                for idx, i in enumerate(save_phrases):
                    f.write(save_names[idx])
                    f.write('\t')
                    f.write(save_doc[idx])
                    f.write('\t')
                    f.write(i)
                    f.write('\n')
        except Exception as e:
            print(e)

    
